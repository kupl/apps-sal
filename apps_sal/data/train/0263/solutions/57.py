
#27

class Solution:
    def knightDialer(self, n: int) -> int:
        prev = [1] * 10
        
        fromMap = {1: {8,6}, 2: {7,9}, 3:{4,8}, 4: {0,3,9}, 5:{}, 6:{0,1,7}, 7:{2,6}, 8:{1,3}, 9:{2,4}, 0:{4,6}}
        
        for i in range(1,n):
            dp = [0] * 10
            for k in range(10):
                for j in fromMap[k]:
                    dp[k] += prev[j]
                    dp[k] %= 10**9 + 7
            
            prev = dp
        
        return sum(prev) % (10**9+7)
