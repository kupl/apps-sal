class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        a = len(A)
        dp = [[0]*a for _ in range(a)] # dp array
        #print(dp)
        index = [-1]*20001#index array
        maximum = 2
        for i in range(0,a):
            dp[i] = [2]*a
            for j in range(i+1, a):
                #print(\"A[i]\",A[i],\"A[j]\",A[j] )
                first = A[i]*2-A[j]
                #print(\"first\",first)
                if first < 0 or index[first]==-1:
                    continue
                else:
                    #print(\"index[first]\",index[first])
                    #print(\"dp[index[first]][i]\",dp[index[first]][i])
                    dp[i][j] = dp[index[first]][i]+1
                    #print(\"dp[i][j]\",dp[i][j])
                    maximum = max(maximum,dp[i][j] ) 
                    #print(\"max\", maximum)
            #print(dp)
            index[A[i]] = i
        return maximum
    
    

