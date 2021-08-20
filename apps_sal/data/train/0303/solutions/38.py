class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        max_sums = [0] * len(arr)
        for i in range(len(arr)):
            if i <= k - 1:
                max_sums[i] = (i + 1) * max(arr[:i + 1])
            else:
                res = 0
                for j in range(1, k + 1):
                    first = max_sums[i - j]
                    second = j * max(arr[i - j + 1:i + 1])
                    res = max(res, first + second)
                max_sums[i] = res
        return max_sums[-1]
