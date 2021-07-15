import math
class Solution:
    def knightDialer(self, N: int) -> int:
        dp = [[[0 for _ in range(3)] for _ in range(4)] for _ in range(N)]
        
        
        direction = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        
        for k in range(N):
            for i in range(4):
                for j in range(3):
                    if k == 0:
                        if (i == 3 and j == 0) or (i == 3 and j == 2):
                            dp[0][i][j] = None
                        else:
                            dp[0][i][j] = 1
                    else:
                        if dp[k-1][i][j] == None:
                            dp[k][i][j] = None
                            continue

                        if i == 1 and j == 1:
                            dp[k][i][j] = 0
                            continue

                        for d in direction:
                            fromi = i + d[0]
                            fromj = j + d[1]
                            #check fromi and fromj are valid
                            if 0 <= fromi <= 3 and 0 <= fromj <= 2 and dp[k-1][fromi][fromj] != None:
                                dp[k][i][j] += dp[k-1][fromi][fromj]
        res = 0
        for i in range(4):
            for j in range(3):
                if dp[-1][i][j] == None:
                    continue
                res += dp[-1][i][j]
        t = pow(10,9)+7
        return res % t
                        
                        
                        

