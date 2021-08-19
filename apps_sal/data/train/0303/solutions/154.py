class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        best_sums = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            curr_max = 0
            for j in range(1, min(k + 1, i + 2)):
                curr_max = max(curr_max, arr[i - j + 1])
                best_sums[i] = max(best_sums[i], best_sums[i - j] + j * curr_max)
        return best_sums[-2]
