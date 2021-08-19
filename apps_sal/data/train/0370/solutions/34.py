class Solution:
    def find(self, g, i):
        # find the group id of element i
        if i in g:
            gid = g[i]
        else:
            gid = g[i] = i

        if gid != i:
            new_gid = self.find(g, gid)
            g[i] = new_gid
        return g[i]

    def merge(self, g, i, j):
        # merge two groups
        gid = self.find(g, i)
        gjd = self.find(g, j)
        if gid != gjd:
            g[gid] = gjd

    def prime_factors(self, x):
        if x == 1:
            return [1]

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
                  67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
                  139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
                  223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
                  293, 307, 311, 313, 317]

        ans = {x}
        idx, p = 0, primes[0]
        while p * p <= x:
            if x % p == 0:
                ans.add(p)
                x //= p
            else:
                idx += 1
                p = primes[idx]
        if x > 1:
            ans.add(x)
        return ans

    def largestComponentSize(self, A: List[int]) -> int:

        n = len(A)
        print(n)
        g = dict()

        for x in A:
            pfs = list(self.prime_factors(x))

            for p in pfs[1:]:
                self.merge(g, pfs[0], p)

        groups = [self.find(g, x) for x in A]
        ans = collections.Counter(groups).most_common(1)
        return ans[0][1]
