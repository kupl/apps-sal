class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        rank = collections.defaultdict(int)
        parent =  collections.defaultdict(int) 
        def find(a):
            if parent[a] == 0: return a
            if parent[a] != a and parent[a] != 0:
                parent[a] = find(parent[a])
            return parent[a]
        def union(a,b):
            a = find(a)
            b = find(b)
            if rank[a] > rank[b]:
                parent[b] = a
                rank[a] += 1
            elif rank[a] <= rank[b]:
                parent[a] = b
                rank[b] += 1
        def prime_set(n):
            for i in range(2, int(sqrt(n))+1):
                # print(n, i)
                if n%i ==0:
                    return prime_set(n//i) | set([i])
            return set([n])
        
        primes = defaultdict(list)
        
        for i, num in enumerate(A):
            ps = prime_set(num)
            # print(ps)
            for p in ps: primes[p].append(i)
        print(primes)
        for p in primes:
            pairs = primes[p]
            for i in range(len(primes[p])-1):
                union(A[pairs[i]], A[pairs[i+1]])
        print((Counter(find(A[i]) for i in range(len(A)))))
        return max(Counter(find(A[i]) for i in range(len(A))).values())

