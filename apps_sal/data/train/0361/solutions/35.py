class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if m == n: return 1
        if n < m:
            m,n = n,m  # so n is bigger
        if m == 1:
            return n
        if m == 2:
            k,rem = divmod(n,2)
            return k + 2*rem
        
        def recurse(h, ct):
            nonlocal Min
            if ct >= Min: return
            if all(x == m for x in h):
                Min = min(Min, ct)
                return
            i = j = min(list(range(n)),key = lambda c: h[c])
            hi = h[i]          
            bound = min(n,i+m-hi)
            while j < bound and h[j] == hi:
                j += 1
            for x in range(j-i, 0, -1):
                recurse(h[:i] + [hi+x]*x + h[i+x:], ct+1)
        
        
        Min = m*n # we initialize to this worst case of all 1x1s
        recurse([0]*n, 0)
        return Min

