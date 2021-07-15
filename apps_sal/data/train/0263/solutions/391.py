class Solution:
    def knightDialer(self, n: int) -> int:
        dc = {0:[4,6],1:[6,8],2:[7,9],3:[4,8],4:[3,9,0],5:[],6:[0,7,1],7:[2,6],8:[1,3],9:[2,4]}
        dp = [[0]*10 for i in range(n+1)]
        for i in range(10):
            dp[1][i]=1
        for i in range(2,n+1):
            for j in range(10):
                for k in range(10):
                    if j in dc[k]:
                        dp[i][j]+=dp[i-1][k]
        return sum(dp[n])%(10**9+7)

