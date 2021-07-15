class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        n = 400
        prime = [True for i in range(n+1)] 
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n+1, p): 
                    prime[i] = False
            p += 1
        prime[0] = False
        prime[1] = False
        prime_set = [p for p in range(n+1) if prime[p]]
        
        cnt = 0
        for i in nums:
            if i == 0:
                continue
            for p in prime_set:
                if p * p > i:
                    break
                if i % p == 0:
                    r = i // p
                    if r == p or r == 1:
                        break
                    r_prime = True
                    for q in prime_set:
                        if q * q > r:
                            break
                        if r % q == 0:
                            if r != q:
                                r_prime = False
                            break
                    if r_prime:  
                        cnt += (p+1) * (r+1)
                    break
                    
        
        for i in nums:
            p = int(i**(1/3) +0.5)
            if prime[p] and p**3 == i:
                cnt += (p * i - 1) // (p - 1)
                print(i, p, p**2, p)
                    
        return cnt
