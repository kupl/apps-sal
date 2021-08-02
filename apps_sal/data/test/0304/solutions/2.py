from collections import Counter
from itertools import product

s = input()

ds = Counter(s)


fac = [1 for i in range(100)]
for i in range(1, 100):
    fac[i] = fac[i - 1] * i

res = 0
for possib in product(*[list(zip([k] * n, list(range(1, n + 1)))) for k, n in list(ds.items())]):
    possib = list(possib)
    non_zero_sum = sum(v for k, v in possib if k != '0')
    total = sum(v for _, v in possib)

    value = non_zero_sum * fac[total - 1]
    for _, v in possib:
        value //= fac[v]

    res += value
print(res)
