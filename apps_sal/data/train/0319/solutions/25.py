class Solution:
    def stoneGameIII(self, cards):
        dp = [0] * 3

        for i in range(len(cards) - 1, -1, -1):
            dp[i % 3] = max(sum(cards[i:i + k]) - dp[(i + k) % 3] for k in [1, 2, 3])

        if dp[0] < 0:
            return 'Bob'
        elif dp[0] > 0:
            return 'Alice'
        else:
            return 'Tie'
