from math import gcd
from collections import defaultdict
N = int(input())
MOD = 10 ** 9 + 7

zero_zero_num = 0
fishes = defaultdict(int)
for i in range(N):
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0:
        zero_zero_num += 1
    elif a == 0:
        fishes[(0, -1)] += 1
    elif b == 0:
        fishes[(1, 0)] += 1
    else:
        g = gcd(a, b)
        a, b = a // g, b // g
        if (a > 0 and b > 0) or (a < 0 and b < 0):
            fishes[(abs(a), abs(b))] += 1
        else:
            a, b = (-a, -b) if a < 0 else (a, b)
            fishes[(a, b)] += 1


ans = 1
keys = list(fishes.keys())
visited = set()
for (kai, kbi) in keys:
    if kbi >= 0:
        kaj, kbj = kbi, -kai
    else:
        kaj, kbj = -kbi, kai

    if ((kai, kbi) in visited) or ((kaj, kbj) in visited):
        continue

    ans *= (1 + (pow(2, fishes[(kai, kbi)], MOD) - 1) + (pow(2, fishes[(kaj, kbj)], MOD) - 1))
    ans %= MOD
    visited.add((kai, kbi))
    visited.add((kaj, kbj))

print(((ans + zero_zero_num - 1) % MOD))

