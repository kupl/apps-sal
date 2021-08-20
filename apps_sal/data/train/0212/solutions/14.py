class Solution:

    def collect(self, lst, st, num, cache):
        if num in cache:
            return cache[num]
        res = 1
        for n1 in lst:
            if n1 ** 2 > num:
                break
            if num % n1 == 0 and num // n1 in st:
                n2 = num // n1
                res_local = self.collect(lst, st, n1, cache) * self.collect(lst, st, n2, cache)
                res += res_local
                if n1 != n2:
                    res += res_local
        mod = 10 ** 9 + 7
        res = res % mod
        cache[num] = res
        return res

    def solve(self, A):
        st = set(A)
        lst = sorted(list(st))
        res = 0
        cache = {}
        mod = 10 ** 9 + 7
        for n in lst:
            res += self.collect(lst, st, n, cache)
        return res % mod

    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        return self.solve(A)
