(n, k) = map(int, input().split())
ans = 0
for i in range(k + 1, n + 1):
    ans += n // i * (i - k)
    if k == 0:
        m = n % i
    else:
        m = n % i - k + 1
    ans = max(ans, ans + m)
print(ans)
