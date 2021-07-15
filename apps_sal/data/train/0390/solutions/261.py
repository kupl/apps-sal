class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        if n == 1:
            return True
        num = 0
        dp = [False] * (1 + n)
        while num * num < n:
            dp[num * num] = True
            num += 1
        if num * num == n:
            return True
            
        for i in range(1, n + 1):
            if dp[i]:
                continue
            j = 1
            while j * j <= i:
                if not dp[i - j * j]:
                    dp[i] = True
                    break
                j += 1
        return dp[n]
                
        
        

