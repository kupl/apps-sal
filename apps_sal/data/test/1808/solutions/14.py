n, k, x = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    if n - i - 1 < k:
        ans += min(a[i], x)
    else:
        ans += a[i]
print(ans)


