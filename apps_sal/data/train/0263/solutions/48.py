class Solution:
    def knightDialer(self, n: int) -> int:
        jump = {1:[6,8], 2:[7,9], 3:[8,4], 4:[0,9,3], 5:[], 6:[7,1,0], 7:[6,2], 8:[3,1], 9:[4,2], 0:[6,4]}
        
        dp = [1]*10
        for _ in range(n-1):
            nxt = [0]*10
            for i in range(10):
                for j in jump[i]:
                    nxt[j] += dp[i]
            dp = nxt
        return sum(dp)%(10**9+7)
    
    

