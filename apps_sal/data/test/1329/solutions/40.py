# 素因数分解
import sys
from itertools import permutations
from collections import defaultdict
from collections import Counter


def soinsu_bunkai(m):
    pf = {}

    for i in range(2, int(m**0.5) + 1):
        while m % i == 0:
            pf[i] = pf.get(i, 0) + 1
            m //= i
    if m > 1:
        pf[m] = 1
    return pf


# 初期入力
input = sys.stdin.readline  # 文字列では使わない
N = int(input())

# Nの階乗の素数列挙
c = defaultdict(int)
for i in range(1, N + 1):
    x = soinsu_bunkai(i)
    for j, v in x.items():
        c[j] += v


ans = set()
for p, q, r in permutations(c.keys(), 3):
    if c[p] >= 74:
        ans.add(p**74)
    if c[p] >= 24 and c[q] >= 2:
        ans.add((p**24) * (q**2))
    if c[p] >= 14 and c[q] >= 4:
        ans.add((p**14) * (q**4))
    if c[p] >= 4 and c[q] >= 4 and c[r] >= 2:
        ans.add((p**4) * (q**4) * (r**2))

print(len(ans))
