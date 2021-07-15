class Solution:
    def knightDialer(self, n: int) -> int:
        limit = 10**9+7
        dp = [[1 for i in range(3)] for j in range(4)]
        dp[3][0],dp[3][2] = 0,0
        direction = [(1,2),(-1,2),(1,-2),(-1,-2),(2,-1),(2,1),(-2,1),(-2,-1)]
        for k in range(n-1):
            temp = [[0 for i in range(3)] for j in range(4)]
            for i in range(4):
                for j in range(3):
                    if i == 3 and j != 1:
                        continue
                    for di,dj in direction:
                        new_i,new_j = di+i,dj+j
                        if 0<= new_i< 4 and 0<= new_j<3:
                            temp[i][j] = (temp[i][j]+dp[new_i][new_j])%limit
            dp = temp[:]
        res = 0
        for i in range(4):
            for j in range(3):
                res+= dp[i][j]
        return res%limit
