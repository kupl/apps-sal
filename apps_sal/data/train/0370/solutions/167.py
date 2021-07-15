class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def get_factors(n):
            factors = set()
            while n % 2 == 0:
                factors.add(2)
                n //= 2
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    factors.add(i)
                    n //= i
            if n > 2:
                factors.add(n)
            return factors
        
        roots = [i for i in range(len(A))]
        
        def find_root(i):
            while i != roots[i]:
                roots[i] = roots[roots[i]]
                i = roots[i]
            return i
        
        primes = defaultdict(list)
        
        for i in range(len(A)):
            factors = get_factors(A[i])
            for n in factors:
                primes[n].append(i)
        
        for values in list(primes.values()):
            for i in range(len(values) - 1):
                roots[find_root(values[i + 1])] = roots[find_root(values[i])]
                
        ans = 0
        counter = defaultdict(int)
        
        for i in range(len(roots)):
            counter[find_root(i)] += 1
            ans = max(ans, counter[find_root(i)])
        
        return ans

