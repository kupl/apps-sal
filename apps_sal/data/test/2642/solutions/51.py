from collections import Counter
import math
MOD = 10**9 + 7
N = int(input())
li = []
zcnt = 0
az, bz = 0, 0
for i in range(N):
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        zcnt += 1
        continue
    if A != 0 and B == 0:
        bz += 1
        continue
    elif A == 0 and B != 0:
        az += 1
        continue
    g = math.gcd(A, B)
    if A < 0 and B < 0:
        li.append((-(A // g), -(B // g)))
    elif A < 0 and B > 0:
        li.append((-(A // g), -(B // g)))
    else:
        li.append((A // g, B // g))
c = Counter(li)
dic = {}
ans = (pow(2, az, MOD) + pow(2, bz, MOD) - 1 + MOD) % MOD
for a, b in c.keys():
    if (a, b) in dic:
        continue
    l, r = (-b, a), (b, -a)
    s = c.get(l, 0) + c.get(r, 0)
    dic[l], dic[r] = 1, 1
    res = (pow(2, c[(a, b)], MOD) + pow(2, s, MOD) - 1 + MOD) % MOD
    ans = (ans * res) % MOD
print((ans - 1 + zcnt) % MOD)
