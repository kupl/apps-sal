class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        mm = [[a for a in arr]]
        for i in range(len(arr) - 1):
            mm.append([0] * len(arr))
        for i in range(1, k):
            for j in range(i, len(arr)):
                mm[i][j] = max(mm[i - 1][j - 1], arr[j])
        dp = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            for j in range(max(k, i)):
                dp[i] = max(dp[i], dp[i - j - 1] + mm[j][i - 1] * (j + 1))
        print(dp)
        return dp[-1]
