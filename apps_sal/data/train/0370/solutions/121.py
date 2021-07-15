class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        # https://leetcode.com/problems/largest-component-size-by-common-factor/discuss/819919/Python-Union-find-solution-explained
        # This question feels like union find but u cannot link together
        # First, find the primes factor of each number
        # And then group together same prime factore
        # The largest group is the largest component
        # But the way to find primes set is a little confusing 
        # It loop from small to large and find the first factor and the primes set for the larger factor
        # If two numbers share the same prime factor, they belong to the same group
        # Then use union find to grouo together
        n = len(A)
        record = [-1]*n
        primes = collections.defaultdict(list)
        def get_primes(i):
            for j in range(2,int(math.sqrt(i))+1):
                if i%j == 0:
                    # And find the primes set for the larger factor
                    return get_primes(i//j) | set([j])
            return set([i])
                
            return res
        def find(a):
            if record[a] < 0:return a
            record[a] = find(record[a])
            return record[a]
        
        
        # U have been wrong on this several times
        # When merge, it is the record[i] == root index, not root val
        def union(i,j):
            a,b = find(i),find(j)
            if a!=b:
                if a<b:
                    record[a] = b
                else:
                    record[b] = a
                
            
        for i, v in enumerate(A):
            primes_set = get_primes(v)
            for j in primes_set:
                primes[j].append(i)
            
        for _,indexes in list(primes.items()):
            for i in range(len(indexes)):
                union(indexes[0],indexes[i])
        
        res = 0
        mapping = collections.defaultdict(set)
        for i in range(n):
            root = find(i)
            mapping[root].add(i)
            if len(mapping[root]) > res:res = len(mapping[root])
        return res

