from collections import defaultdict
from math import gcd
MOD = 1000000007
N = int(input())
zeros = 0
bads = defaultdict(lambda: [0, 0])
for _ in range(N):
    (x, y) = list(map(int, input().split()))
    if x == 0 and y == 0:
        zeros += 1
        continue
    if y < 0 or (y == 0 and x < 0):
        (x, y) = (-x, -y)
    g = gcd(x, y)
    (x, y) = (x // g, y // g)
    if x > 0:
        bads[x, y][0] += 1
    else:
        bads[y, -x][1] += 1
ans = 1
for (k, l) in list(bads.values()):
    ans *= pow(2, k, MOD) - 1 + (pow(2, l, MOD) - 1) + 1
    ans %= MOD
print((ans + zeros - 1) % MOD)
