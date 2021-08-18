from math import gcd
from sys import setrecursionlimit
setrecursionlimit(4100000)
mod = 10 ** 9 + 7
n = int(input())

zeros = 0
d = {}
for i in range(n):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        zeros += 1
    else:
        g = gcd(x, y)
        x, y = x // g, y // g
        if (y < 0) or (y == 0 and x < 0):
            x, y = -x, -y
        else:
            pass
        if x <= 0:
            sq = True
            x, y = y, -x
        else:
            sq = False
        if sq == True:
            if (x, y) in d:
                d[(x, y)][1] += 1
            else:
                d[(x, y)] = [0, 1]
        else:
            if (x, y) in d:
                d[(x, y)][0] += 1
            else:
                d[(x, y)] = [1, 0]


def mod_pow(a: int, b: int, mod: int) -> int:
    if b == 0:
        return 1 % mod
    elif b % 2 == 0:
        return (mod_pow(a, b // 2, mod) ** 2) % mod
    elif b == 1:
        return a % mod
    else:
        return ((mod_pow(a, b // 2, mod) ** 2) * a) % mod


ans = 1
for (a, b), (k, l) in d.items():
    now = 1
    now = (now + mod_pow(2, k, mod) - 1) % mod
    now = (now + mod_pow(2, l, mod) - 1) % mod
    ans = (ans * now) % mod

ans -= 1
zeros = zeros % mod
ans = (ans + zeros) % mod
print(ans)
