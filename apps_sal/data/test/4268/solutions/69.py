import math
(n, d) = list(map(int, input().split()))
l = [list(map(int, input().split())) for l in range(n)]
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        x = 0
        for k in range(d):
            x += (l[i][k] - l[j][k]) ** 2
        y = math.sqrt(x)
        (a, b) = math.modf(y)
        if a == 0:
            ans += 1
print(ans)
