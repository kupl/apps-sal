(n, m, k) = map(int, input().split())
(x, s) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
ans = n * x
for i in range(m):
    l = 0
    r = k
    while r - l > 1:
        mid = l + (r - l) // 2
        if d[mid] <= s - b[i]:
            l = mid
        else:
            r = mid
    if d[l] <= s - b[i]:
        t = a[i] * (n - c[l])
        ans = min(ans, t)
for i in range(k):
    if d[i] <= s:
        ans = min(ans, x * (n - c[i]))
for i in range(m):
    if b[i] <= s:
        ans = min(ans, a[i] * n)
print(ans)
