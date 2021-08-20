import math
(n, d) = list(map(int, input().split()))
xx = []
for i in range(n):
    xx.append(list(map(int, input().split())))


def distance(xx, d, i, j):
    ans = 0
    for u in range(d):
        ans += (xx[i][u] - xx[j][u]) ** 2
    if math.sqrt(ans).is_integer():
        return 1
    else:
        return 0


count = 0
for i in range(n):
    for j in range(i + 1, n):
        count += distance(xx, d, i, j)
print(count)
