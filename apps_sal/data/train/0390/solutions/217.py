class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        base = 1
        steps = []
        dp = [False for i in range(n + 1)]
        for i in range(1, n + 1):
            if base * base <= i:
                steps.append(base * base)
                base += 1
            for step in steps:
                if not dp[i - step]:
                    dp[i] = True
                    break
        return dp[-1]
