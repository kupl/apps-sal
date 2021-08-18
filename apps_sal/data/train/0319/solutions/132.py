class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        N = len(stoneValue)
        stoneValue += [0, 0, 0]
        dp = [-sys.maxsize] * N + [0, 0, 0]
        for i in range(N - 1, -1, -1):
            for k in (1, 2, 3):
                dp[i] = max(dp[i], sum(stoneValue[i:i + k]) - dp[i + k])
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
