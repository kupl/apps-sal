(n, m) = list(map(int, input().split()))
minn_g = [1001] * n
maxx_g = [-1] * n
minn_v = [1001] * m
maxx_v = [-1] * m
size_g = [0] * n
size_v = [0] * m
for i in range(n):
    o = list(map(int, input().split()))
    for j in range(m):
        if o[j] == 1:
            size_g[i] += 1
            size_v[j] += 1
            minn_g[i] = min(minn_g[i], j)
            minn_v[j] = min(minn_v[j], i)
            maxx_g[i] = max(maxx_g[i], j)
            maxx_v[j] = max(maxx_v[j], i)
res = 0
for i in range(n):
    if size_g[i] != 0:
        res += m - size_g[i] - minn_g[i]
        res += maxx_g[i] + 1 - size_g[i]
for i in range(m):
    if size_v[i] != 0:
        res += n - size_v[i] - minn_v[i]
        res += maxx_v[i] + 1 - size_v[i]
print(res)
