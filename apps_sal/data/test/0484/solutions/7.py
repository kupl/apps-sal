import re, sys

n, a, b = list(map(int, input().split()))

d = [tuple(map(int, input().split())) for i in range(n)]

def f(a, b, d):
    ans = []
    if a <= d[0] and b <= d[1]:
        ans.append((d[0] - a, d[1]))
        ans.append((d[0], d[1] - b))
    a, b = b, a
    if a <= d[0] and b <= d[1]:
        ans.append((d[0] - a, d[1]))
        ans.append((d[0], d[1] - b))
    return ans

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for t in f(d[i][0], d[i][1], (a, b)):
            if len(f(d[j][0], d[j][1], t)):
                ans = max(ans, d[i][0] * d[i][1] + d[j][0] * d[j][1])

print(ans)

