from cmath import phase
n = int(input())
xy = sorted([list(map(int, input().split())) for i in range(n)], key=lambda x: phase(x[0] + x[1] * 1j))
xy += xy
ans = 0
for l in range(n):
    a = [0, 0]
    for r in range(l, min(2 * n, l + n)):
        a[0] += xy[r][0]
        a[1] += xy[r][1]
        ans = max(ans, abs(a[0] + a[1] * 1j))
print(ans)
