class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        N = len(stoneValue)
        dp = [0] * (N + 3)
        acc = 0
        for i in range(N - 1, -1, -1):
            acc += stoneValue[i]
            dp[i] = acc - min(dp[i + x] for x in range(1, 4))
        alice = dp[0]
        bob = acc - alice
        if alice > bob:
            return 'Alice'
        elif alice == bob:
            return 'Tie'
        else:
            return 'Bob'
