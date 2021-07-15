class BigCombination(object):
    __slots__ = ["mod", "factorial", "inverse"]

    def __init__(self, mod: int = 10**9+7, max_n: int = 10**6):
        fac, inv = [1], []
        fac_append, inv_append = fac.append, inv.append

        for i in range(1, max_n+1):
            fac_append(fac[-1] * i % mod)

        inv_append(pow(fac[-1], mod-2, mod))

        for i in range(max_n, 0, -1):
            inv_append(inv[-1] * i % mod)

        self.mod, self.factorial, self.inverse = mod, fac, inv[::-1]

    def get_combination(self, n, r):
        return self.factorial[n] * self.inverse[r] * self.inverse[n-r] % self.mod

    def get_permutation(self, n, r):
        return self.factorial[n] * self.inverse[n-r] % self.mod

import math
Big = BigCombination()
n,k = list(map(int,input().split()))
s = 0
for i in range(k):
    if n - k + 1 < i + 1:
      	print('0')
      	continue
    print(((Big.get_combination(n-k+1,i+1) *Big.get_combination(k-1,i))%(10**9+7)))


