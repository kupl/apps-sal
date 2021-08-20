(a, b, c, d) = list(map(int, input().split()))
a = [a, b, c]
a.sort()
ans = 0
if a[1] - a[0] < d:
    ans += a[0] + d - a[1]
if a[2] - a[1] < d:
    ans += a[1] + d - a[2]
print(ans)
