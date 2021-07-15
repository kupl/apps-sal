class UnionFind:
    def __init__(self, N):
        self.parents = [i for i in range(N)]
        self.size = [1]*N

    def find(self, x):
        root = x
        while root != self.parents[root]:
            root = self.parents[root]

        while x != root:
            parent = self.parents[x]
            self.parents[x] = root
            x = parent

        return root

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False

        if self.size[root_a] <= self.size[root_b]:
            self.parents[root_a] = root_b
            self.size[root_b] += self.size[root_a]
        else:
            self.parents[root_b] = root_a
            self.size[root_a] += self.size[root_b]

        return True

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        uf = UnionFind(max(A)+1)
    
        for a in A:
            for factor in range(2, int(math.sqrt(a)) + 1):
                if a % factor == 0:
                    uf.union(a, factor)
                    uf.union(a, a // factor)
                
        group2size = defaultdict(int)
        for a in A:
            group2size[uf.find(a)] += 1
    
        return max(group2size.values())
        

