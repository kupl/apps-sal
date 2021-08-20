class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0]
        for i in range(len(arr)):
            max_sum = -float('inf')
            for j in range(1, k + 1):
                if i - j + 1 < 0:
                    break
                max_sum = max(max_sum, max(arr[i - j + 1:i + 1]) * j + dp[i - j + 1])
            dp.append(max_sum)
        return dp[-1]
