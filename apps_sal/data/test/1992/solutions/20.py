n, m, k = [int(x) for x in input().split()]
a = [int(x) - 1 for x in input().split()]
b = [int(x) - 1 for x in input().split()]
ra = [0] * n
for i, v in enumerate(a):
    ra[v] = i
ans = 0
for v in b:
    i = ra[v]
    ans += i // k + 1
    if i == 0:
        continue
    j = i - 1
    u = a[j]
    ra[u], ra[v] = ra[v], ra[u]
    a[i], a[j] = a[j], a[i]
print(ans)


