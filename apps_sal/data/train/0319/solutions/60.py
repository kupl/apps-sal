class Solution:
    def stoneGameIII(self, sv: List[int]) -> str:
        n=len(sv)
        sv.append(0)
        sv.append(0)
        dp=[0 for _ in range(n+3)]
        for i in range(n-1,-1,-1):
            dp[i]=max(sv[i]-dp[i+1],sv[i]+sv[i+1]-dp[i+2], sv[i]+sv[i+1]+sv[i+2]-dp[i+3])
        # print(dp)
        if dp[0]>0:
            return 'Alice'
        elif dp[0]<0:
            return 'Bob'
        return 'Tie'

                
                

