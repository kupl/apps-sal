class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [[-math.inf, -math.inf] for _ in range(n + 1)]
        dp[-1] = [0, 0]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, min(i + 4, n + 1)):
                if dp[i][0] < dp[j][1] + sum(stoneValue[i:j]):
                    dp[i][0] = dp[j][1] + sum(stoneValue[i:j])
                    dp[i][1] = dp[j][0]
        (alice, bob) = dp[i]
        if alice > bob:
            return 'Alice'
        elif alice < bob:
            return 'Bob'
        else:
            return 'Tie'
