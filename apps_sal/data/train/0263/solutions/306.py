class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [[4,6], [6,8], [7,9], [4,8], [0,3,9], [], [1,7,0], [2,6], [1,3], [2,4]]
        
        dp = [1] * 10
        for _ in range(n-1):
            dp2 = [0] * 10
            for i in range(10):
                dp2[i] = sum(dp[j] for j in moves[i]) % (10**9+7)
                
            dp = dp2
            
        return sum(dp) % (10**9 + 7)

