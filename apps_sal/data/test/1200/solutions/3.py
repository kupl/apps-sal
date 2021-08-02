from fractions import gcd
from functools import reduce

n = int(input())
x = list(map(int, input().split()))
x.sort()

difs = []
for i in range(len(x) - 1):
    difs.append(x[i + 1] - x[i])

dif = reduce(gcd, difs)

mmin = x[0]
mmax = x[-1]
x = set(x)
cnt = (mmax - mmin + dif) // dif - n
print(cnt)
