class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        largest_sums = []
        for i in range(len(A)):
            if i < K:
                largest_sums.append(max(A[:i + 1]) * (i + 1))
                continue
            max_sum = 0
            for j in range(K):
                if i - (j + 1) < 0:
                    continue
                cur_sum = largest_sums[i - j - 1] + max(A[i - j:i + 1]) * (j + 1)
                if cur_sum > max_sum:
                    max_sum = cur_sum
            largest_sums.append(max_sum)
        return largest_sums[-1]
