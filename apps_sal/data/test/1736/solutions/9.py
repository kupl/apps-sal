(n, t) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
r = 0
s = 0
res = 0
for i in range(n):
    if i:
        s -= a[i - 1]
    while r < n and s + a[r] <= t:
        s += a[r]
        r += 1
    res = max(res, r - i)
    r = max(i, r)
print(res)
