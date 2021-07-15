class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        graph = defaultdict(list)
        uf = UnionFind(len(A))
        
        for i, num in enumerate(A):
            prime_factors = set(self.get_prime_factors(num))
            for factor in prime_factors:
                graph[factor].append(i)
        
        for factor in graph:
            indices = graph[factor]
            for i in range(len(indices)-1):
                uf.union(indices[i], indices[i+1])
        
        counter = Counter()
        for i in range(len(A)):
            root = uf.find(i)
            counter[root] += 1
        
        return max(counter.values())
        
    def get_prime_factors(self, num):
        res = []
        factor = 2
        while num >= factor*factor:
            if num % factor == 0:
                res.append(factor)
                num = num // factor
            else:
                factor += 1
        res.append(num)
        return res

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return False
        self.parent[rooty] = rootx
        return True
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
        
            

