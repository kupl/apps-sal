k, n = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
a.append(a[0] + k)

ans = 0
for i in range(n):
    d = a[i + 1] - a[i]
    ans = max(ans, d)

print(k - ans)
