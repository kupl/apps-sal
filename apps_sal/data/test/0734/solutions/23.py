(n, m) = map(int, input().split())
a = sorted([int(i) for i in input().split()])
ans = 0
c = a[n - 1]
if n == 1:
    print(0)
    raise SystemExit
for i in range(n - 1, -1, -1):
    if i > 0 and a[i - 1] < c - 1:
        a[i] -= c - 1 - a[i - 1]
        ans += a[i] - 1
        c = a[i - 1]
    elif a[i] >= c:
        ans += a[i] - c
        if i:
            ans += max(c - 1, 0)
        c -= 1
    c = max(c, 1)
print(ans)
