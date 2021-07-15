class Solution:
    def soupServings(self, N: int) -> float:
        if N>=10000:
            return 1.0
        L=N//25+1 if N%25>0 else N//25
        res=dict()
        res[0,0]=0.5
        for l in range(1,L+1):
            res[l,0]=0.0
            res[0,l]=1.0
        for m in range(1,L+1):
            for n in range(1,L+1):
                res[m,n]=0.25*(res[max([m-4,0]),n]+res[max([m-3,0]),max([n-1,0])]+res[max([m-2,0]),max(n-2,0)]+res[max(m-1,0),max(n-3,0)])
        return res[L,L]
