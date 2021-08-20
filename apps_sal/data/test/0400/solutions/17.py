(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += a[i] // 10
    a[i] %= 10
a.sort()
a = a[::-1]
i = 0
while i != n and a[i] != 0 and (m > 0):
    c = 10 - a[i]
    if m >= c:
        m -= c
        ans += 1
    else:
        m = 0
    i += 1
ans += m // 10
if ans < 10 * n:
    print(ans)
else:
    print(10 * n)
