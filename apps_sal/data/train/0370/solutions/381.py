class UnionFind:
    def __init__(self, N):
        self.N = N
        self.rank = [1 for i in range(N)]
        self.parent = [i for i in range(N)]
    def find(self, x):
        y = x
        while x != self.parent[x]:
            x = self.parent[x]
        self.parent[y] = x
        return x
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
        return True
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def gcd(a, b): #Find gcd of (a, b) in logarithmic time
            if b > a:
                a, b = b, a
            while b:
                a = a % b
                a, b = b, a
            return a
        def union_all(x):
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    uf.union(x, i)
                    uf.union(x, x//i)
                    # if x == 100 and i == 5:
                    #     print(\"hey\")
                    #     print(uf.find(100), uf.find(5))
        uf = UnionFind(100001)
        max_size = 1
        for i in range(len(A)):
            union_all(A[i])
        d = Counter()
        for i in range(len(A)):
            d[uf.find(A[i])] += 1
            max_size = max(max_size, d[uf.find(A[i])])
            # print(A[i], uf.find(A[i]))
        # print(uf.parent[5])
        # print(uf.parent[100])
        # print(uf.find(9), uf.find(8), uf.find(1))
        return max_size
            
            
            
            
                
        

