n, m, k = map(int, input().split())
a = list(map(int, input().split()))
m -= 1
be = -1
af = n + 1
for i in range(n):
    if a[i] <= k and a[i] != 0 and i < m and i > be:
        be = i
    elif a[i] <= k and a[i] != 0 and i > m and i < af:
        af = i
if be == -1:
    print((af - m) * 10)
elif af == n + 1:
    print((m - be) * 10)
else:
    print(10 * min(m - be, af - m))
