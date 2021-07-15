class Solution:
    class UnionFind:
        def __init__(self, n, m):
            self.n = n
            self.m = m
            self.rank = [0] * n
            self.parent = [n for i in range(n)]
            self.counts = [0] * n
            self.counts_num = [0] * 100005
            
        def set(self, idx):
            self.rank[idx] = 1
            self.parent[idx] = idx
            self.counts[idx] = 1
            self.counts_num[self.counts[idx]] += 1
            if self.find(idx-1) != self.n:
                self.unite(idx, idx-1)
            if self.find(idx+1) != self.n:
                self.unite(idx, idx+1)
            
        def find(self, idx):
            if idx == self.n or self.parent[idx] == idx:
                return idx
            self.parent[idx] = self.find(self.parent[idx])
            return self.parent[idx]
            
        def unite(self, idx, idx2):
            if idx < 0 or idx2 < 0 or idx >= self.n or idx2 >= self.n:
                return
            root = self.find(idx)
            root2 = self.find(idx2)
            if root == root2:
                return
            self.counts_num[self.counts[root]] -= 1
            self.counts_num[self.counts[root2]] -= 1
            if self.rank[root] > self.rank[root2]:
                self.parent[root2] = root
                self.rank[root] += 1
                self.counts[root] += self.counts[root2]
                self.counts[root2] = 0
            else:
                self.parent[root] = root2
                self.rank[root2] += 1
                self.counts[root2] += self.counts[root]
                self.counts[root] = 0
            self.counts_num[self.counts[root]] += 1
            self.counts_num[self.counts[root2]] += 1

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        uf = self.UnionFind(n, m)
        ans = -2
        for i, num in enumerate(arr):
            uf.set(num - 1)
            if uf.counts_num[m] > 0:
                ans = max(ans, i)
            
        return ans + 1

