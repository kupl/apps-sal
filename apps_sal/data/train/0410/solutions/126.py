class Solution:
    def getKth(self, lo, hi, k):
        #
        memo = { 1:0 }
        def power(x):
            if x in memo:
                return memo[x]
            n = memo[x] = 1 + power( (3*x+1) if x&1 else (x >> 1) )
            return n
        #
        A = [ (power(x),x) for x in range(lo,hi+1) ]
        return sorted(A)[k-1][1]

