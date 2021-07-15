class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        parent = [i for i in range(len(A))]
        rank = [0 for i in range(len(A))]
        
        def prime_factors(n):
            # for i in range(2, int(math.sqrt(n))+1):
                # if n % i == 0:
                    # return prime_factors(n//i) | set([i])
            # return set([n])
            primes = set()
            d = 2
            while d <= sqrt(n):
                if n % d == 0:
                    primes.add(d)
                    n //= d
                else:    
                    d += 1
            if n > 1:
                primes.add(n)
            return primes        
                    
        def find(n):    
            p = parent[n]
            if p == n:
                return p
            parent[n] = find(parent[n])
            return parent[n]

        def merge(n1, n2):
            r1 = find(n1)
            r2 = find(n2)
            
            if r1 == r2:
                return
            
            if rank[r1] < rank[r2]:
                parent[r1] = r2
            elif rank[r1] > rank[r2]:
                parent[r2] = r1
            else:    
                parent[r1] = r2
                rank[r2] += 1
                
        prime_indeces = defaultdict(list)
        for i, n in enumerate(A):
            primes = prime_factors(n)
            for p in primes:
                prime_indeces[p].append(i)
            
        print(prime_indeces)    
        # print(parent)
        for p, indeces in list(prime_indeces.items()):
            for i in range(len(indeces)-1):
                # print('merging', A[indeces[i]], A[indeces[i+1]])
                merge(indeces[i], indeces[i+1])
                # print(parent)        
                
                
        count_map = dict()
        best = 0        
        
        for i in parent:
            i = find(i)
            if i in count_map:
                count_map[i] += 1
            else:
                count_map[i] = 1
                
            best = max(best, count_map[i])
        # print(count_map)    
            
        return best

