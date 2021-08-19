(N, C) = map(int, input().split())
x = [0] * N
v = [0] * N
for i in range(N):
    (x[i], v[i]) = map(int, input().split())
lcal = [0] * N
lmax = [0] * N
rcal = [0] * N
rmax = [0] * N
rcal[0] = v[0] - x[0]
rmax[0] = rcal[0]
for i in range(1, N):
    rcal[i] = rcal[i - 1] + v[i] - x[i] + x[i - 1]
    rmax[i] = max(rmax[i - 1], rcal[i])
lcal[0] = v[N - 1] - (C - x[N - 1])
lmax[0] = lcal[0]
for i in range(1, N):
    lcal[i] = lcal[i - 1] + v[N - i - 1] + x[N - i - 1] - x[N - i]
    lmax[i] = max(lmax[i - 1], lcal[i])
ans = 0
for i in range(N - 1):
    ans = max(ans, rcal[i], rcal[i] + lmax[N - i - 2] - x[i])
ans = max(ans, rcal[N - 1])
for i in range(N - 1):
    ans = max(ans, lcal[i], lcal[i] + rmax[N - i - 2] - (C - x[N - i - 1]))
ans = max(ans, lcal[N - 1])
print(ans)
