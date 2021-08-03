class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        suffix_sums = [0] * (len(A) + 1)
        for i in range(len(A) - 1, -1, -1):
            suffix_sums[i] = A[i] + suffix_sums[i + 1]

        memo = {}

        def largest_starting_at(i, new_k):
            if i == len(A):
                return 0
            if new_k == 1:
                return suffix_sums[i] / (len(A) - i)
            if (i, new_k) in memo:
                return memo[i, new_k]
            best = 0
            for size in range(1, len(A) - i):
                best = max(
                    best,
                    (suffix_sums[i] - suffix_sums[i + size]) / size + largest_starting_at(i + size, new_k - 1)
                )
            memo[i, new_k] = best
            return memo[i, new_k]

        return largest_starting_at(0, K)
