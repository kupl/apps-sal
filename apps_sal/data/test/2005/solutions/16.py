n, n1, n2 = map(int, input().split())
a = sorted(list(map(int, input().split())))
ans = 0.0
s = 0.0
for i in range(min(n1, n2)):
    s += a[n - 1 - i]
s /= min(n1, n2)
ans += s
s = 0.0
for i in range(min(n1, n2), min(n1, n2) + max(n1, n2)):
    s += a[n - 1 - i]
s /= max(n1, n2)
ans += s
print(ans)
