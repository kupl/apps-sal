class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        max_p = int(2 + max(A) ** 0.5)
        primes = [2,3,5,7,11,13,17,19]
        
        for num in range(20, max_p):
            for p in primes:
                if p * p > num:
                    primes.append(num)
                    break
                if num % p == 0:
                    break
        
        
        prime_factors = collections.defaultdict(list)
        members = collections.defaultdict(list)
        
        for num in A:
            num0 = num 
            for prime in primes:
                if prime ** 2 > num:
                    if num > 1:
                        prime_factors[num0].append(num)
                        members[num].append(num0)
                    break
                if num % prime == 0:
                    prime_factors[num0].append(prime)
                    members[prime].append(num0)
                while num % prime == 0:
                    num //= prime
        
        # bipartite graph
        # print(prime_factors)
        # print(members)
         
        visited_primes = set()
        ans = 0
        for p in members.keys():
            if p in visited_primes:
                continue
            visited_members = set()
            
            q_prime = collections.deque([p])
            
            while q_prime:
                pp = q_prime.popleft()
                
                for m in members[pp]:
                    
                    if m in visited_members:
                        continue
                    visited_members.add(m)
                    
                    for ppp in prime_factors[m]:
                        
                        if ppp in visited_primes:
                            continue
                        visited_primes.add(ppp)
                        
                        q_prime.append(ppp)
                     
            
            ans = max(ans, len(visited_members))
        return ans
