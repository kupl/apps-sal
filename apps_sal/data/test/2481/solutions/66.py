from collections import defaultdict
import sys
readline = sys.stdin.readline

H, W = map(int, readline().split())
C = [None] * 10
for i in range(10):
    C[i] = list(map(int, readline().split()))

for k in range(10):
    for i in range(10):
        for j in range(10):
            C[i][j] = min(C[i][j], C[i][k] + C[k][j])

wall = defaultdict(int)
for i in range(H):
    for w in list(map(int, readline().split())):
        wall[w] += 1

ans = 0
for key, value in wall.items():
    if key == -1:
        continue
    ans += value * C[key][1]

print(ans)
