from collections import Counter
n, x, y = list(map(int, input().split()))
c = Counter()
for i in range(1, n):
    for j in range(i + 1, n + 1):
        dist = min(abs(j - i), abs(x - i) + 1 + abs(j - y), abs(y - i) + 1 + abs(j - x))
        c[dist] += 1

for k in range(1, n):
    print((c[k]))
