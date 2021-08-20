class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        length = len(arr)
        dp = [0] * (length + 1)
        maxval = [[0] * length for _ in range(length)]
        for i in range(length):
            for j in range(i, length):
                if i == j:
                    maxval[i][j] = arr[i]
                else:
                    maxval[i][j] = max(maxval[i][j - 1], arr[j])
        for i in range(1, length + 1):
            temp = 0
            for t in range(1, k + 1):
                temp = max(temp, dp[i - t] + maxval[i - t][i - 1] * t)
            dp[i] = temp
        return dp[-1]
