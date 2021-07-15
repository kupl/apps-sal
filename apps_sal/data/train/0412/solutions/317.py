class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = {}
        
        for i in range(1, f+1):
            dp[i] = 1
            
        for i in range(d-1):
            temp = {}
            for val in dp:
                for dice in range(1, f+1):
                    if val + dice <= target:
                        temp[val+dice] = temp.get(val+dice, 0) + dp[val]
            dp = temp
                
        if not target in dp:
            return 0
        return dp[target]  % (10**9 + 7)
                    

