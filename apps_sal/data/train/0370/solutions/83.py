class Primes:
    def __init__(self, N):
        self.N = N
        self.primes = [0]*(N+1)
        self.get_primes()
    
    def get_primes(self):
        for i in range(2, self.N+1):
            if self.primes[i]==0:
                self.primes[i] = i
                upto = self.N//i
                for j in range(2, upto+1):
                    if self.primes[i*j] == 0:
                        self.primes[i*j] = i
    
    def __call__(self, n):
        # num = n
        if n<=2:
            return {n}
        p = []
        while n>=2:
            lp = self.primes[n]
            p.append(lp)
            n =  n//lp
        # print(num,\":\", p)
        return set(p)

class DisjointSet:
    def __init__(self, primes):
        self.primes = primes
        self.count = 1
        
    def union(self, setB):
        # print(\"org:\", self.primes)
        # print(\"union with:\", setB.primes)
        self.primes |= setB.primes
        self.count += setB.count
        # print(\"after union:\", self.primes)
        
        
    
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        disjoint_sets = []
        Factors = Primes(max(A))
        rank = [1]*(len(A)+1)
        parent = [-1]*(len(A)+1)
        m = dict()
        curr_count = 0
        
        def get_parent(x):
            if parent[x]==-1: return x
            parent[x] = get_parent(parent[x])
            # print(f\"parent of {x} is {parent[x]}\")
            return parent[x]
        
        def union(x, y):
            parx = get_parent(x)
            pary = get_parent(y)
            if parx==pary: return
            if rank[parx]>=rank[pary]:
                rank[parx] += rank[pary]
                parent[pary] = parx
            else:
                rank[pary] += rank[parx]
                parent[parx] = pary
            # print(x,\":\",\"parent\", paar)
        
            
        for i,val in enumerate(A):
            # union = []
            val_primes = Factors(val)
            # for i, ds in enumerate(disjoint_sets):
            #     diff_set = val_primes - ds.primes
            #     if len(diff_set) < len(val_primes):
            #         union.append(i)
            #         val_primes = diff_set
            # # if len(val_primes)>0:
            # #     new_set = DisjointSet(val_primes)
            # #     disjoint_sets.append(new_set)
            # #     union.append(-1)
            # temp_set = DisjointSet(val_primes)
            # for ds in union:
            #     temp_set.union(disjoint_sets[ds])
            #     # disjoint_sets[union[-1]].union(disjoint_sets[ds])
            #     # curr_count = max(curr_count, disjoint_sets[union[-1]].count)
            # for ds in reversed(union):
            #     disjoint_sets.pop(ds)
            # disjoint_sets.append(temp_set)
            
            for prime in val_primes:
                if prime in m:
                    union(m[prime],i)
                else:
                    m[prime]=i
                    # print(prime, \":\", i)
        curr_count = max(rank)
        return curr_count
                
                

