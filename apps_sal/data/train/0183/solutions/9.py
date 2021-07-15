mi = -100000000000
dp = [[mi]*(505) for i in range(505)]
def steps(i,j,lis1,lis2):
    best = mi
    if i<0 or j<0:
        return 0
    elif dp[i][j]!=mi:
        return dp[i][j]
    if i==0:
        for _ in range(j+1):
            best = max(lis1[i]*lis2[_] , best)
        dp[i][j]=best
        return dp[i][j]
    if j==0:
        for _ in range(i+1):
            best = max(lis1[_]*lis2[j] , best)
        dp[i][j]=best
        return best

    best = max(steps(i-1,j,lis1,lis2) , steps(i,j-1,lis1,lis2) , lis1[i]*lis2[j] + steps(i-1,j-1,lis1,lis2) , lis1[i]*lis2[j])
    dp[i][j]=best
    return dp[i][j]
class Solution:
    def maxDotProduct(self, lis1: List[int], lis2: List[int]) -> int:
        n = len(lis1)
        m = len(lis2)
        for i in range(501):
            for j in range(501):
                dp[i][j]=mi
        steps(n-1,m-1,lis1,lis2)
        return dp[n-1][m-1]
        
        

