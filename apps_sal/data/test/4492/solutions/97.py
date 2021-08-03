N, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(N - 1):
    if a[i] + a[i + 1] > x:
        y = a[i] + a[i + 1] - x
        ans += y
        a[i + 1] = max(0, a[i + 1] - y)
print(ans)
