class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def pfactorization(a):
            N = a
            if a >= 2 and a % 2 == 0:  # treat 2 alone
                Gp[2].append(N)
                Gn[N].append(2)
                while a % 2 == 0:
                    a //= 2
            for d in range(3, math.floor(a**(1 / 2)) + 1, 2):  # possible odd numbers
                if d > a:
                    break
                if a % d == 0:
                    Gn[N].append(d)
                    Gp[d].append(N)
                    while a % d == 0:
                        a //= d
            if a > 1:  # check if what remains is itself a prime
                Gp[a].append(N)
                Gn[N].append(a)
        # Find the prime factors of the current number using Gn,
        # For each prime factor, find all the numbers excluding self who have this prime factor
        # They should all be connected

        def dfs(curr):
            if curr in seenNodes:
                return 0
            seenNodes.add(curr)
            total = 1
            for p in Gn[curr]:
                if p in seenPrimes:
                    continue
                seenPrimes.add(p)
                for owner in Gp[p]:
                    total += dfs(owner)
            return total
        # This graph contains numbers in the list sharing the a prime factor, the key is that prime factor
        Gp = defaultdict(list)
        # This graph stores prime factors of each number in the list
        Gn = defaultdict(list)
        for a in A:
            pfactorization(a)
        seenPrimes, seenNodes = set(), set()
        return max([dfs(a) for a in A])
# Time Complexity : O(sqrt(max(A)*max(A))
