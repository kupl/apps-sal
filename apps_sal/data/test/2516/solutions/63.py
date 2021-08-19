"""
s=1817181712114 なら
4
10
100
2000
10000
700000
1000000
80000000
100000000
7000000000
10000000000
800000000000
1000000000000
の数列とみて, 各々%Pを取ってzero sum range
P=2,5がコーナー
"""
from collections import Counter


def make_modlist(Len, mod):
    modlist = [0] * Len
    modlist[0] = 1
    for i in range(1, Len):
        modlist[i] = 10 * modlist[i - 1] % mod
    return modlist


(n, p) = map(int, input().split())
a = list(map(int, input()))
ans = 0
a.reverse()
if p == 2 or p == 5:
    for i in range(n):
        if a[i] % p == 0:
            ans += n - i
else:
    d = make_modlist(n, p)
    b = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = a[i] * d[i] % p
    for i in range(1, n + 1):
        b[i] += b[i - 1]
        b[i] %= p
    for i in Counter(b).values():
        ans += i * (i - 1) // 2
print(ans)
