(n, k, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
s = sum(a)
ans = 0
for i in range(n + 1):
    t = s * i
    cur = (k + 1) * i
    if t > m:
        break
    t = m - t
    for j in range(k):
        x = min(t // a[j], n - i)
        t -= x * a[j]
        cur += x
    ans = max(ans, cur)
print(ans)
