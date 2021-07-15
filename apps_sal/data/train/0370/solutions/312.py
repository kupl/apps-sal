class Solution:
    
    def primeDecompose(self, num):
        factor = 2
        prime_factors = []
        while num >= factor*factor:
            if not num % factor:
                prime_factors.append(factor)
                num //= factor
            else:
                factor += 1
        prime_factors.append(num)
        return prime_factors
    
    def largestComponentSize(self, A: List[int]) -> int:
        
        # 1. Find set of numbers that belongs to each prime factor
        factors = collections.defaultdict(set)
        for num in A:
            prime_factors = self.primeDecompose(num)
            for p in prime_factors:
                factors[p] |= set([num])
        
        primes = list(factors)
        
        group_id = 0
        group = {}
        prime_id = {}
        updated = set(primes)
        first_round = True
        
        for i in range(len(primes)):
            a = primes[i]
            
            if a not in factors:
                continue

            for b in list(factors):
                
                if b == a:
                    continue
                    
                if len(factors[b]) == 1:
                    del factors[b]
                elif factors[a] & factors[b]:
                    factors[a] |= factors[b]
                    del factors[b]

        return len(factors[max(factors, key = lambda f: len(factors[f]))])
