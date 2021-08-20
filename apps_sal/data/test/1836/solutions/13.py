(n, m) = list(map(int, input().split()))
d = [0] * n
f = [[] for i in range(n)]
for i in range(m):
    a = list(map(int, input().split()))
    d[a[0] - 1] += 1
    d[a[1] - 1] += 1
    a.sort()
    f[a[1] - 1] += [a[0] - 1]
k = [1] * n
res = 0
for i in range(n):
    for j in f[i]:
        k[i] = max(k[i], k[j] + 1)
    res = max(res, k[i] * d[i])
print(res)
