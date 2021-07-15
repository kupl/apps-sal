class UnionFind:
    def __init__(self, n):
        self.p = []
        self.size = [1] * n
        for i in range(n):
            self.p.append(i)
        self.max_union_size = 1
        
    def union(self, X, Y):
        px, py = self.find(X), self.find(Y)
        if px == py:
            return
        elif self.size[px] < self.size[py]:
            self.p[px] = py
            self.size[py] += self.size[px]
            self.max_union_size = max(self.max_union_size, self.size[py])
        else:
            self.p[py] = px
            self.size[px] += self.size[py]
            self.max_union_size = max(self.max_union_size, self.size[px])

    def find(self, X): 
        if self.p[X] != X:
            self.p[X] = self.find(self.p[X])
        return self.p[X]
    
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def get_prime_factors(num):
            n = num
            d = 2
            while d * d <= n:
                if n % d == 0:
                    yield d
                while n % d == 0:
                    n //= d
                d += 1
            if n > 1:
                yield n
        
        factors_to_nums = collections.defaultdict(list)
        for i, a in enumerate(A):
            for f in get_prime_factors(a):
                factors_to_nums[f].append(i) # save the index of the number in A, which is easier to generate UF
        
        uf = UnionFind(len(A))
        for idx_of_num in factors_to_nums.values():
            for i in range(1, len(idx_of_num)):
                uf.union(idx_of_num[0], idx_of_num[i])
        
        return uf.max_union_size

''' 
# lingnan 写的DisjointSet，还没有看
class DisjointSet:
    def __init__(self, n):
        self.parent = [-1] * n
        self.max_size = 1
    
    
    def find(self, x):
        root = x
        while self.parent[root] >= 0:
            if self.parent[self.parent[root]] >= 0:
                self.parent[root] = self.parent[self.parent[root]]
            root = self.parent[root]
        return root
    
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        
        if x_root != y_root:
            if self.parent[x_root] > self.parent[y_root]:
                x_root, y_root = y_root, x_root
            
            self.parent[x_root] += self.parent[y_root]
            self.parent[y_root] = x_root
            self.max_size = max(self.max_size, -self.parent[x_root])
    

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def get_prime_factors(num):
            n = num
            d = 2
            while d * d <= n:
                if n % d == 0:
                    yield d
                while n % d == 0:
                    n //= d
                d += 1
            if n > 1:
                yield n
        
        f_to_i = collections.defaultdict(list)
        for i, a in enumerate(A):
            for f in get_prime_factors(a):
                f_to_i[f].append(i)
        
        ds = DisjointSet(len(A))
        for indexes in f_to_i.values():
            for i in range(1, len(indexes)):
                ds.union(indexes[0], indexes[i])
        
        return ds.max_size
'''
