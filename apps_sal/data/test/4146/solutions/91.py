import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
V = list(map(int, input().split()))

v1 = []
v2 = []

for i, v in enumerate(V):
    if i % 2 == 0:
        v1.append(v)
    else:
        v2.append(v)

v1c = Counter(v1).most_common()
v2c = Counter(v2).most_common()

k1, v1 = v1c[0][0], v1c[0][1]
k2, v2 = v2c[0][0], v2c[0][1]

ans = N
if k1 == k2:
    ans -= v1
    m = 0
    if len(v1c) >= 2:
        m = max(m, v1c[1][1])
    if len(v2c) >= 2:
        m = max(m, v2c[1][1])
    ans -= m
else:
    ans -= v1 + v2

print(ans)
