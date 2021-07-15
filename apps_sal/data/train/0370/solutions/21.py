class DSU:
    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1] * N

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        
        if xr == yr: return
        
        if self.size[xr] >= self.size[yr]:
            self.size[xr] += self.size[yr]
            self.size[yr] = self.size[xr]
            self.parent[yr] = xr
        else:
            self.size[yr] += self.size[xr]
            self.size[xr] = self.size[yr]
            self.parent[xr] = yr


class Solution:
        
    def largestComponentSize(self, A: List[int]) -> int:
        N = len(A)
        max_A = max(A)
        is_prime = [True] * (max_A+1)
        index = {x: i for i, x in enumerate(A)}
        dsu = DSU(N)
        
        for factor in range(2, max_A + 1):
            if is_prime[factor]:
                multiplier = factor << 1
                previous = index.get(factor)
                
                while multiplier <= max_A:
                    is_prime[multiplier] = False
                    if multiplier in index:
                        if previous is not None: 
                            dsu.union(previous, index.get(multiplier))
                        previous = index[multiplier]
                        
                    multiplier += factor
                    
                    
        # Browse DSU for result
        return max(dsu.size)
