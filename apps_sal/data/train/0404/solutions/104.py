class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        dp = [[0 for y in range(len(A))] for x in range(K)]
        add=0
        pref=[0 for i in range(len(A))]
        
        for x in range(len(A)):
            add+=A[x]
            pref[x]=add
        # print(pref)
        for x in range(len(A)):
            dp[0][x] = (pref[x]/(x+1))
        for y in range(1,K):
            dp[y][0] = A[0]
        for x in range(1,K):
            for y in range(1,len(A)):
                val1 = (pref[y]/(y+1))
                maxi = val1
                # print(\"hi\")
                for z in range(y):
                    val = dp[x-1][z] + ((pref[y]-pref[z])/(y-z))
                    # print(x,y,z,val)
                    maxi=max(maxi,val)
                dp[x][y]=maxi
        # print(dp)
        return (dp[-1][-1])
                

