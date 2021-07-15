class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n + 1)]
        #dp[i] denotes can a player win when i stones are present in the pile
        dp[1] = True
        for i in range(2, n + 1):
            j = 1
            while j*j <= i:
                if not dp[i - j*j]:
                    dp[i] = True
                    break
                    
                j += 1
        
        # print(dp)
        return dp[n]
