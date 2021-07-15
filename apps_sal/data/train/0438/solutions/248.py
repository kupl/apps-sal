class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        class DSU:
            def __init__(self, n, m):
                self.parent = [i for i in range(n)]
                self.size = [0] * n
                self.m = m
                self.cntm = 0
                
            def add(self, x):
                self.size[x] = 1
                if self.m == 1:
                    self.cntm += 1
                self.unite(x - 1, x)
                self.unite(x, x + 1)

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def unite(self, x, y):
                if x < 0 or self.size[x] == 0 or y == len(self.size) or self.size[y] == 0:
                    return 
                px, py = self.find(x), self.find(y)
                self.cntm -= self.size[px] == self.m
                self.cntm -= self.size[py] == self.m

                if self.size[px] < self.size[py]:
                    px, py = py, px
                self.size[px] += self.size[py]
                self.parent[py] = px
                self.cntm += self.size[px] == self.m
                
            
        n = len(arr)
        dsu = DSU(n, m)
        latest = -1
        
        for i in range(n):
            dsu.add(arr[i] - 1)
            if dsu.cntm:
                latest = i + 1
        return latest

