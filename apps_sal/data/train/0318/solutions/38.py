class Solution:
    def maxSizeSlices(self, w: List[int]) -> int:
        n_picks = len(w)//3
        
        dp1 = [[0 for _ in range(len(w))] for _ in range(n_picks+1)]
        dp2 = [[0 for _ in range(len(w))] for _ in range(n_picks+1)]
        
        for i in range(1,n_picks+1):
            for j in range(1,len(w)):
                
                if j == 1:
                    dp1[i][j] = w[j-1]
                    dp2[i][j] = w[j]
                    continue
                dp1[i][j] = max(w[j-1] + dp1[i-1][j-2],dp1[i][j-1])
                dp2[i][j] = max(w[j] + dp2[i-1][j-2],dp2[i][j-1])
        
        return max(dp1[n_picks][len(w)-1],dp2[n_picks][len(w)-1])
    

