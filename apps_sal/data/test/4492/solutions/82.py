(n, x) = map(int, input().split())
a = list(map(int, input().split()))
s = [0] * (n - 1)
ans = 0
if a[0] > x:
    ans += a[0] - x
    a[0] = x
for i in range(n - 1):
    s[i] = a[i] + a[i + 1]
for i in range(n - 2):
    if s[i] > x:
        t = s[i] - x
        s[i + 1] -= t
        s[i] = x
        ans += t
if s[n - 2] > x:
    ans += s[n - 2] - x
print(ans)
