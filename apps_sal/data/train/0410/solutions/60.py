class Solution:
    def getKth(self, lo, hi, k):
        def power(x):
            if x&1:
                return 0 if x==1 else 1+power( 3*x + 1 )
            return 1+power(x >> 1)
        A = [ (power(x),x) for x in range(lo,hi+1) ]
        return sorted(A)[k-1][1]
