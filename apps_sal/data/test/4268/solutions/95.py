import math


def solve(y, z):
    res = 0
    for i in range(len(y)):
        res += (y[i] - z[i])**2
    return math.sqrt(res)


n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        dist = solve(x[i], x[j])
        if int(dist) == dist:
            ans += 1
print(ans)
