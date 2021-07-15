n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
if k >= 3:
    print(max(a))
    return
if k == 1:
    print(min(a))
    return
mn = [10 ** 9 + 1] * n
mn[0] = a[0]
for i in range(1, n):
    mn[i] = min(mn[i - 1], a[i])
mnn = 10 ** 9 + 1
ans = - 10 ** 9 - 1
for i in range(n - 1, -1, -1):
    mnn = min(mnn, a[i])
    ans = max(ans, max(mnn, mn[i - 1]))
print(ans)
