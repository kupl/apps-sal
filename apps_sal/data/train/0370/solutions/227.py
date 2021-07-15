import math

class DSU:
    def __init__(self, N):
        self.p = list(range(N))
        self.sizes = [1]*N

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return
        
        if self.sizes[x_root] > self.sizes[y_root]:
            self.p[x_root] = y_root
            self.sizes[y_root] += self.sizes[x_root]
        else:
            self.p[y_root] = x_root
            self.sizes[x_root] += self.sizes[y_root]

class Solution:
    def prime_set(self, n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return self.prime_set(n//i) | set([i])
        return set([n])

    def largestComponentSize(self, A: List[int]) -> int:               
        prime_map = {}
        for i in range(len(A)):
            P = self.prime_set(A[i])
            for p in P:
                if p not in prime_map:
                    prime_map[p] = []
                prime_map[p].append(i)
        
        DSU_groups = DSU(len(A))
        for _, group in prime_map.items():
            for i in range(len(group)-1):
                DSU_groups.union(group[i], group[i+1])
        
        return max(DSU_groups.sizes)
