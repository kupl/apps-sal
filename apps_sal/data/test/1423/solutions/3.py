import sys

N, L, R = list(map(int, input().split()))
a = list(map(int, input().split()))
b = [0] * N
c = list(map(int, input().split()))
d = [i for i in range(N)]

z = [list(t) for t in zip(c, a, b, d)]
z = sorted(z)

z[0][2] = L
last = z[0][2] - z[0][1]

for i in range(1, N):
    z[i][2] = max(last + 1 + z[i][1], L)
    if z[i][2] > R:
        print(-1)
        return
    last = z[i][2] - z[i][1]

z = sorted(z, key=lambda t: t[3])
_, _, res, _ = list(zip(*z))
print(*res)

