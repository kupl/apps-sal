import math
(n, r) = map(int, input().split())
x = list(map(int, input().split()))
y = [r]
for i in range(1, len(x)):
    cur = r
    for j in range(i):
        d = abs(x[i] - x[j])
        if d <= 2 * r:
            cur = max(cur, y[j] + math.sqrt(4 * r ** 2 - d ** 2))
    y.append(cur)
print(*y)
