class Solution:
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def step(n,i) -> int:
            i = i + 1
            if n == 1:
                return i - 1

            if n % 2:
                i = step(3*n+1,i)
            else:
                i = step(n//2,i)
            return i

        a = 0
        l = []
        for i in range(lo,hi+1):
            a = step(i,0)
            l.append((i,a))
            
        l = sorted(l,key=lambda x:x[1])    
        return l[k-1][0]
