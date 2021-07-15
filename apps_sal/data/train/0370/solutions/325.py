class UF:
    def __init__(self,size):
        self.d = [i for i in range(size+1)]
    def find(self,m):

        if self.d[m] != m:
            self.d[m] = self.find(self.d[m])
        return self.d[m]
    def union(self,m,n):
        pm = self.find(m)
        pn = self.find(n)

        self.d[pm] = pn

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        uf = UF(max(A))
        for a in A:
            for factor in range(2,int(a**0.5)+1):
                if a % factor == 0:
                    uf.union(a,factor)
                    uf.union(a,a//factor)
        ret = 0
        C = collections.Counter()
        for a in A:
            group_id = uf.find(a)
            C[group_id] += 1
            ret = max(ret,C[group_id])
        return ret
