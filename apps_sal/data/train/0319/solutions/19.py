class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        postsum, dp = 0, [0] * (len(stoneValue) + 3)
        for i in range(len(stoneValue) - 1, -1, -1):
            postsum += stoneValue[i]
            dp[i] = postsum - min(dp[i + 1], dp[i + 2], dp[i + 3])
        alice, bob = dp[0], postsum - dp[0]
        if alice == bob:
            return 'Tie'
        if alice > bob:
            return 'Alice'
        return 'Bob'
