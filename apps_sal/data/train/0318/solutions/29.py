class Solution:
    def maxSizeSlices(self, w: List[int]) -> int:
        k = len(w)//3
        
        dp1 = [[0]*(len(w)) for _ in range(k+1)]
        dp2 = [[0]*(len(w)) for _ in range(k+1)]
        
        for n in range(1,k+1):
            for i in range(1,len(w)):
                
                if i==1:
                    dp1[n][i] = w[i-1]
                    dp2[n][i] = w[i]
                    continue
                
                dp1[n][i] = max(dp1[n-1][i-2]+w[i-1],dp1[n][i-1])
                dp2[n][i] = max(dp2[n-1][i-2]+w[i],dp2[n][i-1])
        return max(dp1[-1][-1],dp2[-1][-1])
