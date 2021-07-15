class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # [99,68,70,77,35,52,53,25,62]
        n = len(A)
        dsu = DSU(n)
        prime_dict = defaultdict(list)
        for i, num in enumerate(A):
            primes = self.find_p(num)
            for p in primes:
                prime_dict[p].append(i)
        for _, p_list in list(prime_dict.items()):
            for j in range(len(p_list)):
                dsu.union(p_list[0], p_list[j])
        return max(Counter(dsu.find(x) for x in range(n)).values())
    
    def find_p(self, x):
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return self.find_p(x // i) | set([i])
        return set([x])
    
    


class DSU:
    def __init__(self, n):
        self.sets = list(range(n))
        
    def find(self, x):
        if self.sets[x] != x:
            root = self.find(self.sets[x])
            self.sets[x] = root
            return root
        return x
    
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.sets[yr] = xr
        
        
                
            
        
            
        
   
    

   

