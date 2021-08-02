n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
ret = 0
for i in range(m):
    cur = 0
    for j in range(i, n):
        if j % m == i:
            cur = max(0, cur)
            cur -= k
        cur += a[j]
        ret = max(ret, cur)
print(ret)
