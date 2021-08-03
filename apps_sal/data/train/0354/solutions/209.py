MOD = int(1e9 + 7)


class Solution:
    def get(self, n, d, l):
        if n == 1:
            return 5 if l == 0 else 6

        try:
            return self.cache[(n, d, l)]
        except KeyError:
            ret = 0
            for e in range(6):
                if e == d:
                    if l > 0:
                        ret += self.get(n - 1, d, l - 1)
                        ret %= MOD
                else:
                    ret += self.get(n - 1, e, self.limits[e] - 1)
                    ret %= MOD
            self.cache[(n, d, l)] = ret
            return ret

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        self.limits = rollMax
        self.cache = {}

        for nn in range(2, n - 1 + 1):
            for d in range(6):
                for l in range(self.limits[d] - 1 + 1):
                    self.get(nn, d, l)
        ret = 0
        for d in range(6):
            ret += self.get(n - 1, d, self.limits[d] - 1)
            ret %= MOD
        return ret
