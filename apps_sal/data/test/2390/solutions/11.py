n, c = list(map(int, input().split()))
x = []
v = []
for i in range(n):
    xi, vi = list(map(int, input().split()))
    x.append(xi)
    v.append(vi)
l1 = [0]
l2 = [0]
r1 = [0]
r2 = [0]
vtotal = 0
for i in range(n):
    vtotal += v[i]
    l1.append(max(l1[-1], vtotal - x[i]))
    l2.append(max(l2[-1], vtotal - 2 * x[i]))
vtotal = 0
for i in range(n - 1, -1, -1):
    vtotal += v[i]
    r1.append(max(r1[-1], vtotal - (c - x[i])))
    r2.append(max(r2[-1], vtotal - 2 * (c - x[i])))
ans = 0
for i in range(n + 1):
    ans = max(ans, l1[i] + r2[n - i], l2[i] + r1[n - i])
print(ans)
