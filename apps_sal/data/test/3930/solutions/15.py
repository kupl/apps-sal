from itertools import accumulate, product

import math


def R(): return map(int, input().split())


n, k = R()
arr, acc = list(accumulate(R())), dict()
acc[0] = 1
res = 0
rk, rks = 1, []
if abs(k) > 1:
    while rk < 10 ** 15:
        rks.append(rk)
        rk *= k
else:
    rks = [1] if k == 1 else [1, -1]

for x in arr:
    for rk in rks:
        res += acc.get(x - rk, 0)
    acc[x] = acc.get(x, 0) + 1
print(res)
