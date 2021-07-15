from collections import defaultdict

n, x, y = map(int, input().split())

d = defaultdict(int)

for i in range(1, n):
    for j in range(i + 1, n + 1):
        d[min(j - i, abs(x - i) + abs(y - j) + 1)] += 1

for i in range(1, n):
    print(d[i])
