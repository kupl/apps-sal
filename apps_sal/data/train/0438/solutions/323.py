class DisjointUnionSets:
    def __init__(self,n):
        self.rank = [0] * n 
        self.parent = [0] * n
        self.n = n
        self.makeSet()

    def makeSet(self):
        for i in range(self.n):
            self.parent[i] = i
        
    def find(self ,x): 
        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x]); 
        return self.parent[x]; 
    
    def union(self, x, y): 
        xRoot = self.find(x)
        yRoot = self.find(y)
   
        if (xRoot == yRoot): 
            return; 
  
        if (self.rank[xRoot] < self.rank[yRoot]):
            self.parent[xRoot] = yRoot
            self.rank[yRoot]+=self.rank[xRoot]
        else: 
            self.parent[yRoot] = xRoot; 
            self.rank[xRoot]+=self.rank[yRoot]



class Solution:
    def findLatestStep(self, arr, m: int) -> int:
        n, ans = len(arr), -1
        uf = DisjointUnionSets(n)
        
        for step, i in enumerate(arr):
            i-=1
            uf.rank[i] = 1
            for j in (i - 1, i + 1):
                if 0 <= j < n:
                    if uf.rank[uf.find(j)] == m:
                        ans = step
                    if uf.rank[j]:
                        uf.union(i, j)
        
        for i in range(n):
            if uf.rank[uf.find(i)] == m:
                return n
        return ans

