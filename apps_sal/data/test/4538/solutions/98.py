import math
count = 0
n, d = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]
for i in range(n):
    if math.sqrt(x[i] ** 2 + y[i] ** 2) <= d:
        count += 1
print(count)

