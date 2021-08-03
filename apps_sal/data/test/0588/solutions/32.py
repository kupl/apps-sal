from math import atan2, pi

n = int(input())
e = []

for _ in range(n):
    x, y = list(map(int, input().split()))
    r = atan2(y, x)
    if r < 0:
        r += pi * 2
    e.append([r, x, y])

e.sort()

ans = 0
for i in range(n):
    e.append([e[i][0] + pi * 2, e[i][1], e[i][2]])
    ans = max(ans, (e[i][1] ** 2 + e[i][2] ** 2) ** 0.5)

if n == 1:
    print(ans)
    return

for L in range(n):
    x = e[L][1]
    y = e[L][2]
    for R in range(L + 1, L + n):
        x += e[R][1]
        y += e[R][2]
        ans = max(ans, (x ** 2 + y ** 2) ** 0.5)

print(ans)
