(N, C) = map(int, input().split())
x = []
v = []
for i in range(N):
    (xi, vi) = map(int, input().split())
    x.append(xi)
    v.append(vi)
l1 = [0]
l2 = [0]
r1 = [0]
r2 = [0]
vtotal = 0
for i in range(N):
    vtotal += v[i]
    l1.append(max(l1[-1], vtotal - x[i]))
    l2.append(max(l2[-1], vtotal - 2 * x[i]))
vtotal = 0
for i in range(N - 1, -1, -1):
    vtotal += v[i]
    r1.append(max(r1[-1], vtotal - (C - x[i])))
    r2.append(max(r2[-1], vtotal - 2 * (C - x[i])))
ans = 0
for i in range(N + 1):
    ans = max(ans, l1[i] + r2[N - i], l2[i] + r1[N - i])
print(ans)
