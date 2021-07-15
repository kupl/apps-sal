# O(n) dp[n] = !dp[n-1] or !dp[n-4] ...
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [-1] * (n+1)
        dp[0] = 0
        return self.can_win(n, dp)
    
    def can_win(self, n, dp):
        if dp[n] != -1:
            return dp[n]
        root = 1
        cur = n - root ** 2
        while cur >= 0:
            dp[cur] = self.can_win(cur, dp)
            if dp[cur] == 0:
                dp[n] = 1
                return 1
            root += 1
            cur = n - root ** 2
        dp[n] = 0
        return dp[n]
