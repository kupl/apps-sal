class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        upper_p = max(nums)
        is_prime = [1] * (upper_p + 1)
        primes = []
        for p in range(2, upper_p + 1):
            if not is_prime[p]:
                continue
            primes.append(p)
            for multi in range(2 * p, upper_p + 1, p):
                is_prime[multi] = 0
        primes_set = set(primes)
        p_par = {p: p for p in primes}
        p_cnt = {p: 0 for p in primes}

        def find_par(ind):
            path = []
            while p_par[ind] != ind:
                path.append(ind)
                ind = p_par[ind]
            for mid in path:
                p_par[mid] = ind
                p_cnt[ind] += p_cnt[mid]
                p_cnt[mid] = 0
            return ind

        def union(p1, p2):
            par1 = find_par(p1)
            par2 = find_par(p2)
            if par1 != par2:
                p_par[par2] = par1
                p_cnt[par1] += p_cnt[par2]
                p_cnt[par2] = 0
            return

        for num in nums:
            if num == 1:
                continue
            factors = []
            for p in primes:
                if p * p > num:
                    break
                if num % p == 0:
                    factors.append(p)
                    while num % p == 0:
                        num //= p
            if num in primes_set:
                factors.append(num)

            for other_p in factors[1:]:
                union(factors[0], other_p)
            p_cnt[find_par(factors[0])] += 1

        return max(p_cnt.values())
