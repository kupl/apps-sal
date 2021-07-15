class Solution:
    def knightDialer(self, n: int) -> int:
        dp=[[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[4,2]]
        ct=[1]*10

        while n-1:
            tmp=[]
            for i in range(10):
                tmp+=[sum(ct[j] for j in dp[i])]
            ct=tmp
            n-=1

        return sum(ct)%(10**9 + 7)

