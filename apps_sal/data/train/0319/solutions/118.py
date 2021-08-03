class Solution:
    def stoneGameIII(self, cards):
        dp = [float('-inf')] * (len(cards))

        for i in range(len(dp) - 1, -1, -1):
            if len(dp) - 1 - i >= 3:
                dp[i] = max(sum(cards[i:i + 3]) - dp[i + 3], sum(cards[i:i + 2]) - dp[i + 2], sum(cards[i:i + 1]) - dp[i + 1])
            elif len(dp) - 1 - i == 2:
                dp[i] = max(sum(cards[i:i + 3]), sum(cards[i:i + 2]) - dp[i + 2], sum(cards[i:i + 1]) - dp[i + 1])
            elif len(dp) - 1 - i == 1:
                dp[i] = max(sum(cards[i:i + 2]), sum(cards[i:i + 1]) - dp[i + 1])
            elif len(dp) - 1 - i == 0:
                dp[i] = cards[i]
        print(dp)
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
