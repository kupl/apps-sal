class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        # idea: 0. dp[i, j] is the max number of uncrossed lines in A[0,i] and B[0,j]
        #       1. init: fill dp with 0
        #       2. transition function: loop(expand) B for each in A
        #           dp[i][j] = max(dp[i-1][j],dp[i][j-1]) to have at least the same number supposing when A[i] was expanded, it won't be connected; or B[j] was expanded, it won't be connected;
        #           then if B[j-1] == A[i-1], dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
        # time: O( len(A) x len(B) )
        # space:O( len(A) x len(B) )
        
        dp: List[List[int]] = [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                if B[j-1] == A[i-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
        return dp[len(A)][len(B)]
        
        
        
        

