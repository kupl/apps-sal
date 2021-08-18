class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        numStones = len(stoneValue)
        dp = [-float('inf')] * numStones
        for i in range(numStones - 1, -1, -1):
            localTotal = 0
            for j in range(i, min(i + 3, numStones)):
                localTotal += stoneValue[j]
                otherPlayerMax = dp[j + 1] if j + 1 < numStones else 0
                dp[i] = max(dp[i], localTotal - otherPlayerMax)
        winner = 'Alice' if dp[0] > 0 else 'Bob' if dp[0] < 0 else 'Tie'
        return winner
