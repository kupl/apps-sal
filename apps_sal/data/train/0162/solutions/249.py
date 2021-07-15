class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        table={}
        def helper(t1, t2, i,j, table):
            if table.get((i,j)) != None:
                return table[(i,j)]
            
            n = len(t1)
            m = len(t2)
            
            if m <=j or n <= i:
                return 0;     
            
            v = t1[i]
            idx = t2.find(v, j)
            if idx != -1:
                r = max(helper(t1, t2, i+1, j, table), helper(t1, t2, i+1, idx+1, table)+1)
                table[(i,j)] = r 
            else:
                r = helper(t1, t2, i+1,j, table)
                table[(i,j)] = r
            return table[(i,j)]
        
        return helper(text1, text2, 0, 0, table)
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        dp=[]
        for v in range(n+1):
            dp.append([-1]*(m+1))
        
        dp[0][0] = 0
        for i in range(n+1):
            dp[i][0] = 0
        for j in range(m+1):
            dp[0][j] = 0
        for i in range(1,n+1):
            for j in range(1, m+1):
                v1=text1[i-1]
                v2 = text2[j-1]
                if v1 == v2:
                    dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[n][m]

