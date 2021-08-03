class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        l = len(stoneValue)
        dp = [0] * (l + 1)
        for i in range(l - 1, -1, -1):
            val = stoneValue[i]
            dp[i] = val - dp[i + 1]
            if i + 1 < l:
                val += stoneValue[i + 1]
                dp[i] = max(dp[i], val - dp[i + 2])
            if i + 2 < l:
                val += stoneValue[i + 2]
                dp[i] = max(dp[i], val - dp[i + 3])
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] == 0:
            return 'Tie'
        else:
            return 'Bob'
