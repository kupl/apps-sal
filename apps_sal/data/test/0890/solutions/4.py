def gray(n):
    if n == 1:
        return ['0', '1']
    l1 = gray(n - 1)
    l2 = reversed(l1)
    l1 = [a + '0' for a in l1]
    l2 = [a + '1' for a in l2]
    return l1 + l2


n, l, r, x = list(map(int, input().split()))
a = list(map(int, input().split()))
ps = gray(n)
ans = 0
for i in ps:
    ma = -1
    mi = 10000000
    s = 0
    k = 0
    for j in range(n):
        if i[j] == '1':
            k += 1
            s += a[j]
            mi = min(mi, a[j])
            ma = max(ma, a[j])
    if s >= l and s <= r and ma - mi >= x and k > 1:
        ans += 1
print(ans)
