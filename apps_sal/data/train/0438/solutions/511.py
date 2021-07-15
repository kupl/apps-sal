from bisect import *
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        arr = [i - 1 for i in arr]
        p = [i for i in range(len(arr))]
        gsize = [0 for _ in range(len(arr))]
        
        def fp(n):
            nonlocal p
            if n == p[n]:
                return p[n]
            else:
                p[n] = fp(p[n])
                return p[n]
            
        def gs(n):
            return gsize[fp(n)]
        
        ms = set()
        def uu(a, b):
            nonlocal ms
            pa = fp(a)
            pb = fp(b)
            
            
            if gs(pa) == m:
                ms.add(pa)
            if gs(pb) == m:
                ms.add(pb)
                
            if pa == pb:
                return
            try:
                ms.remove(pa)
            except:
                pass
            try:
                ms.remove(pb)
            except:
                pass
            
            gsize[pb] += gsize[pa]
            p[pa] = p[pb]
            if gs(pb) == m:
                ms.add(pb)
            
        
        filled = set()
        ans = -2
        for i, n in enumerate(arr):
            gsize[n] = 1
            uu(n, n)
            if n > 0 and n - 1 in filled:
                uu(n, n - 1)
                
                
            if n < N - 1 and n + 1 in filled:
                uu(n, n + 1)

            filled.add(n)
            if len(ms) > 0:
                ans = i
        return ans + 1
                
        

