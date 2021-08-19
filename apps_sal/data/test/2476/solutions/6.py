from itertools import accumulate
import sys


def f(m, k):
    if m == 0:
        return 0
    if m < k:
        return 0
    z = 0
    if acc[m] // k >= c[m]:
        return acc[m] // k
    else:
        return f(m - 1, k - 1)


readline = sys.stdin.readline
n = int(input())
a = [int(i) for i in readline().split()]
res = [0] * (n + 1)
for i in a:
    res[i] += 1
c = [0]
for i in res:
    if i > 0:
        c.append(i)
c.sort()
l = len(c) - 1
acc = list(accumulate(c))
res = [n] + [acc[m] // c[m] for m in range(1, l + 1)]
m = l
for k in range(1, n + 1):
    k -= l - m
    if res[m] >= k:
        print(acc[m] // k)
    else:
        while res[m] < k:
            m -= 1
            k -= 1
        print(acc[m] // k)
