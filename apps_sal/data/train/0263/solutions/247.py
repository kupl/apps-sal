class Solution:
    
    def knightDialer(self, n: int) -> int:
        
        valid_moves = {0: (4, 6), 
                       1:(8, 6), 
                       2:(7,9),
                       3:(4,8),
                       4:(0, 3, 9),
                       5:(),
                       6:(0, 1, 7),
                       7:(2, 6),
                       8:(1, 3),
                       9:(2, 4),
                      }
        
        dp = [[0]*10 for _ in range(n)]
        for c in range(10):
            dp[0][c] = 1
        if n > 1:
            for c in range(10):            
                dp[1][c] = len(valid_moves[c])
            
        
        for i in range(2, n):
            for j in range(10):
                valid = valid_moves[j]
                #print (\"computing i: {0}, j:{1} with valid:{2}\".format(i, j, valid))
                dp[i][j] = sum([dp[i-1][r] for r in valid])
        # print (dp)        
        # print (  sum(dp[n-1]) % (10**9+7))
        
        return sum(dp[n-1]) % (10**9+7)

