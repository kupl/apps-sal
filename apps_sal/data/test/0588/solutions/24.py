from cmath import phase
N = int(input())
XY = sorted([list(map(int, input().split())) for i in range(N)], key=lambda x: phase(x[0] + x[1] * 1j))
XY += XY
ans = 0
for l in range(N):
    a = [0, 0]
    for r in range(l, min(2 * N, l + N)):
        a[0] += XY[r][0]
        a[1] += XY[r][1]
        ans = max(ans, abs(a[0] + a[1] * 1j))
print(ans)
