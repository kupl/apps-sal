from itertools import accumulate
from collections import Counter


def solve(n):
    return n * (n - 1) // 2


s = input()[::-1]
MOD = 2019
rest = []
for (i, x) in enumerate(s):
    if i == 0:
        tmp = 1
    else:
        tmp = tmp * 10 % MOD
    rest.append(int(x) * tmp % MOD)
result = [x % MOD for x in list(accumulate(rest))]
zero = result.count(0)
c = Counter(result)
c = list(c.values())
print(sum([solve(x) for x in c if x >= 2]) + zero)
