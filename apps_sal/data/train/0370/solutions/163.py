class DUS(object):
    
    def __init__(self, n):
        self.p = [ *list(range(n)) ]
        self.size = [1] * n
        
    def Find(self, x):
        if self.p[x] == x:
            return x
        tmp = []
        while self.p[x] != x:
            tmp.append(x)
            x = self.p[x]
        for t in tmp:
            self.p[t] = x
        return x
    
    def Union(self, x, y):
        xr = self.Find(x)
        yr = self.Find(y)
        if xr != yr:
            self.p[yr] = xr
            self.size[xr] += self.size[yr]
            self.size[yr] = 0
        return 
    

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        
        def PFD(num):
            ret = set()
            if num % 2 == 0:
                ret.add(2)
                while num % 2 == 0:
                    num //= 2
            for i in range(3, int(num ** 0.5)+1 , 2 ):
                if num % i == 0:
                    ret.add(i)
                    while num % i == 0:
                        num //= i
            if num > 2:
                ret.add(num)
            return ret
        
        dic = {}
        dus = DUS(len(A))
        for idx, a in enumerate(A):
            for p in PFD(a):
                if p in dic:
                    dus.Union(dic[p], idx)
                dic[p] = idx
        
        return max(dus.size)
        
        

