from math import sqrt, ceil
from collections import defaultdict
(n, *aa) = map(int, open(0).read().split())
MOD = 10 ** 9 + 7


def factors(x):
    d = defaultdict(int)
    while x % 2 == 0:
        d[2] += 1
        x //= 2
    for i in range(3, ceil(sqrt(x)) + 2, 2):
        while x % i == 0:
            d[i] += 1
            x //= i
    if x > 1:
        d[x] += 1
    return d


factors_of_aa = list(map(factors, aa))
factors_of_lcm = defaultdict(int)
for factors_of_a in factors_of_aa:
    for k in factors_of_a:
        factors_of_lcm[k] = max(factors_of_lcm[k], factors_of_a[k])
lcm = 1
for (factor, cnt) in factors_of_lcm.items():
    lcm *= pow(factor, cnt, MOD)
ans = 0
for factors_of_a in factors_of_aa:
    to_add = lcm
    for (factor, cnt) in factors_of_a.items():
        to_add *= pow(factor, -cnt, MOD)
        to_add %= MOD
    ans += to_add
    ans %= MOD
print(ans)
