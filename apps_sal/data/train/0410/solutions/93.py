class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(x):
            if x==1: return 0
            if x%2==0:
                return power(x>>1)+1
            else:
                return power(x*3+1)+1
       
        x=sorted([i for i in range(lo,hi+1)],key=power)
        return x[k-1]
