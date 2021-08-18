'''input
3
1 1
2 2
3 1

'''
import sys
from collections import defaultdict as dd
mod = 998244353


def ri(flag=0):
    if flag == 0:
        return [int(i) for i in sys.stdin.readline().split()]
    else:
        return int(sys.stdin.readline())


n = ri(1)

one = []
sec = []
take = []
for i in range(n):
    a, b = ri()
    one.append(a)
    sec.append(b)
    take.append((a, b))

ans = 1
temp = 1

for i in range(1, n + 1):
    ans = (ans * i) % mod

take.sort()

cnt1 = 0
cnt2 = 0


c1 = dd(int)
c2 = dd(int)
c3 = dd(int)


status = 1

for i in range(1, n):
    if take[i][1] < take[i - 1][1]:
        status = 0

for i in one:
    c1[i] += 1
for i in sec:
    c2[i] += 1
for i in take:
    c3[i] += 1

ok1 = 1
ok2 = 1
ok3 = 1


fac = [1 for i in range(3 * 10**5 + 1)]

for i in range(1, 3 * 10**5 + 1):
    fac[i] = (fac[i - 1] * i) % mod

for i in c1:
    ok1 = (ok1 * fac[c1[i]]) % mod

for i in c2:
    ok2 = (ok2 * fac[c2[i]]) % mod

for i in c3:
    ok3 = (ok3 * fac[c3[i]]) % mod

if status == 0:
    ok3 = 0

print((ans - ok1 - ok2 + ok3) % mod)
