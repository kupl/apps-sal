class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        cnt = dict([(num, 1) for num in A])
        par = dict([(num, num) for num in A])

        def find(num):
            nonlocal par
            if par[num] != num:
                par[num] = find(par[num])
            return par[num]

        def union(num, num2):
            root, root2 = find(num), find(num2)
            if root == root2:
                return
            if root > root2:
                root, root2 = root2, root
            par[root2] = root
            cnt[root] = cnt[root] + cnt[root2]
            cnt[root2] = 0

        primes = [2]
        i = 3
        maxA = max(A)
        while i * i <= 100000:
            is_prime = True
            for prime in primes:
                if i % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(i)
            i += 1
        A = sorted(A)
        prime_set = {}
        for num in A:
            prime_set[num] = set()
            tmp = num
            for prime in primes:
                can_div = False
                while tmp % prime == 0:
                    tmp /= prime
                    can_div = True
                if can_div:
                    prime_set[num].add(prime)
                if prime * prime > num:
                    break
            if tmp > 1:
                prime_set[num].add(tmp)
        prime_nums = {}
        for num in prime_set:
            for p in prime_set[num]:
                prime_nums.setdefault(p, [])
                prime_nums[p].append(num)

        for prime, nums in prime_nums.items():
            roots = set(find(num) for num in nums)
            if len(roots) <= 1:
                continue
            roots = sorted(list(roots))
            for root in roots[1:]:
                union(roots[0], root)
        return max(cnt.values())
