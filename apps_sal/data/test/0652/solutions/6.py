from collections import *
ans = 0
d = Counter()
n = int(input())
p = [tuple(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if p[i] < p[j]:
            x1, y1 = p[i]
            x2, y2 = p[j]
        else:
            x1, y1 = p[j]
            x2, y2 = p[i]
        x, y = x2 - x1, y2 - y1
        ans += d[(x, y)]
        d[(x, y)] += 1
print(ans // 2)
