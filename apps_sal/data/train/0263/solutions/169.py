class Solution:
    def knightDialer(self, n: int) -> int:
        dp=[[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[4,2]]
        ct=[1]*10

        while n-1:           

            ct=[sum(ct[j] for j in i) for i in dp]
                   
            n-=1

        return sum(ct)%(10**9 + 7)

