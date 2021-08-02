from operator import mul
from functools import reduce
from collections import Counter

a, b, c = list(map(int, input().split()))
mod = 2 ** 30

prime = [None] * 100

for i in range(2, 101):
    if prime[i - 1] is None:
        for j in range(i, 101, i):
            prime[j - 1] = i


d = {}
result = 0
for ai in range(1, a + 1):
    for bi in range(1, b + 1):
        for ci in range(1, c + 1):
            n = ai * bi * ci
            res = d.get(n)

            if res is None:
                cd = Counter()

                n_ai = ai
                while prime[n_ai - 1] is not None:
                    cd[prime[n_ai - 1]] += 1
                    n_ai //= prime[n_ai - 1]

                n_bi = bi
                while prime[n_bi - 1] is not None:
                    cd[prime[n_bi - 1]] += 1
                    n_bi //= prime[n_bi - 1]

                n_ci = ci
                while prime[n_ci - 1] is not None:
                    cd[prime[n_ci - 1]] += 1
                    n_ci //= prime[n_ci - 1]

                res = reduce(mul, [x + 1 for x in list(cd.values())], 1)
                d[n] = res

            result += res

print(result % mod)
