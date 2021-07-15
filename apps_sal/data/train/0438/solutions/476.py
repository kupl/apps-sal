class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        bits = [0] * len(arr)
        uf = UnionFind(bits)
        step = 0
        ans = -1
        for real_n in arr:
            step += 1
            # print(\"step\", step)
            n = real_n-1
            bits[n] = 1
            uf.father[n] = n
            uf.cnt[n] = 1
            uf.cntFreq[1] += 1
            # print(bits)
            if n-1 >= 0 and bits[n-1] == 1:
                uf.union(n, n-1)  
            if n+1 < len(bits) and bits[n+1] == 1:
                uf.union(n, n+1) 
            # print(uf.cntFreq)
            if uf.cntFreq[m] > 0:
                ans = step
        return ans
            
class UnionFind:
    def __init__(self, bits):
        self.len = len(bits)
        self.father = [-1] * (self.len)
        self.cnt = [0] * (self.len)
        self.cntFreq = collections.Counter()

                    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        cntP = self.cnt[rootP]
        cntQ = self.cnt[rootQ]
        if rootP != rootQ:
            self.father[rootP] = rootQ
            self.cntFreq[self.cnt[rootP]] -= 1
            self.cntFreq[self.cnt[rootQ]] -= 1
            self.cntFreq[cntP+cntQ] += 1
            self.cnt[rootQ] = cntP+cntQ
        
    def find(self, p):
        rootP = self.father[p]
        while rootP != self.father[rootP]:
            rootP = self.father[rootP]
        self.father[p] = rootP
        return rootP

