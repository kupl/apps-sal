from collections import defaultdict
from math import gcd
N = int(input())
MOD = 10 ** 9 + 7
d = defaultdict(lambda: [0, 0])
zeros = 0
for _ in range(N):
    (x, y) = list(map(int, input().split()))
    if x == 0 and y == 0:
        zeros += 1
    elif x == 0:
        d[0, 0][0] += 1
    elif y == 0:
        d[0, 0][1] += 1
    else:
        if y < 0:
            x = -x
            y = -y
        g = gcd(abs(x), abs(y))
        x //= g
        y //= g
        if x < 0:
            d[y, -x][0] += 1
        else:
            d[x, y][1] += 1
ans = 1
for (k, v) in list(d.items()):
    ans *= pow(2, v[0], MOD) + pow(2, v[1], MOD) - 1
    ans %= MOD
ans = (ans + zeros - 1) % MOD
print(ans)
