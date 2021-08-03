from collections import defaultdict
from collections import Counter
from math import gcd
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
p = 10**9 + 7
used = defaultdict(list)

n = int(input())

ctr = Counter()
az = bz = zz = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    if a == b == 0:
        zz += 1
    elif a == 0:
        az += 1
    elif b == 0:
        bz += 1
    else:
        g = gcd(a, b)
        a, b = a // g, b // g
        if b < 0:
            a *= -1
            b *= -1
        ctr[(a, b)] += 1
        used[(a, b)] = False

ans = 1

# 仲の悪いグループ対ごとに処理する
for (a1, b1), v1 in list(ctr.items()):
    if used[(a1, b1)]:
        continue
    a2, b2 = -b1, a1
    if b2 < 0:
        b2 *= -1
        a2 *= -1
    v2 = ctr[(a2, b2)]

    r = (pow(2, v1, p) + pow(2, v2, p) - 1) % p
    ans *= r
    ans %= p
    used[(a1, b1)] = True
    used[(a2, b2)] = True

# 片方が0のクループ対
r = (pow(2, az, p) + pow(2, bz, p) - 1) % p
ans *= r
ans %= p

ans += zz  # 0匹のケースは禁止されている
ans -= 1  # 0匹のケースは禁止されている
ans %= p
print(ans)
