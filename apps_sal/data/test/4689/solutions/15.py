k, n = map(int, input().split())
a = list(map(int, input().split()))

ans = 10000000
for i in range(n - 1):
    ans = min(k - (a[i + 1] - a[i]), ans)
ans = min(ans, a[n - 1] - a[0])
print(ans)
