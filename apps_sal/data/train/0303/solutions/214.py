class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n+1)
        dp[1] = arr[0]
        for i in range(2, n+1):
            dp[i] = dp[i-1] + arr[i-1]
            cur_max = arr[i-1]
            for j in range(1, k+1): ## j: number of elements in the last group
                cur_max = max(cur_max, arr[i-j])
                if i-j>=0:
                    dp[i] = max(dp[i], dp[i-j]+j*cur_max)
        return dp[n]
