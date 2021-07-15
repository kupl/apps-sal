class Solution:
    def maxSumAfterPartitioning(self, arr, k: int) -> int:
        n = len(arr)
        mask = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(i, n):
                mask[i][j] = max(arr[j], mask[i][j - 1] if j > i else 0)

        for i in range(n):
            for j in range(i, n):
                mask[i][j] = (j + 1 - i) * mask[i][j]
                
        dp = [0]*n
        for i in range(n):
            for h in range(1,k+1):
                dp[i]= max((dp[i-h] if i-h>=0 else 0)+(mask[i-h+1][i] if i-h+1<n else 0), dp[i])
        return dp[-1]
