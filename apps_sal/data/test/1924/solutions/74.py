def f_many_many_paths():
    class Combination(object):
        """参考: https://harigami.net/contents?id=5f169f85-5707-4137-87a5-f0068749d9bb"""
        __slots__ = ['mod', 'factorial', 'inverse']

        def __init__(self, max_val_arg: int = 10**6, mod: int = 10**9 + 7):
            fac, inv = [1], []
            fac_append, inv_append = fac.append, inv.append

            for i in range(1, max_val_arg + 1):
                fac_append(fac[-1] * i % mod)

            inv_append(pow(fac[-1], mod - 2, mod))

            for i in range(max_val_arg, 0, -1):
                inv_append((inv[-1] * i) % mod)

            self.mod, self.factorial, self.inverse = mod, fac, inv[::-1]

        def combination(self, n, r):
            if n < 0 or r < 0 or n < r:
                return 0
            return self.factorial[n] * self.inverse[r] * self.inverse[n - r] % self.mod

    R1, C1, R2, C2 = [int(i) for i in input().split()]
    comb = Combination(R2 + C2 + 2).combination

    def g(r, c):
        return comb(r + c + 2, r + 1) - 1

    return (g(R2, C2) - g(R1 - 1, C2) - g(R2, C1 - 1) + g(R1 - 1, C1 - 1)) % (10**9 + 7)


print(f_many_many_paths())
