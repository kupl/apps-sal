(n, c) = map(int, input().split())
x = [0]
v = [0]
su = [0] * (n + 1)
for i in range(n):
    (xx, vv) = map(int, input().split())
    x.append(xx)
    v.append(vv)
    su[i + 1] = su[i] + v[i + 1]
lmax = [0] * (n + 2)
rmax = [0] * (n + 2)
for i in range(n):
    lmax[i + 1] = max(lmax[i], su[i + 1] - x[i + 1])
    rmax[n - i] = max(rmax[n - i + 1], su[n] - su[n - i - 1] - (c - x[n - i]))
ans = 0
for i in range(n):
    ans = max(ans, su[i + 1] - 2 * x[i + 1] + rmax[i + 2])
    ans = max(ans, su[n] - su[n - i - 1] - 2 * (c - x[n - i]) + lmax[n - i - 1])
ans = max(ans, max(lmax[n], rmax[1]))
print(ans)
