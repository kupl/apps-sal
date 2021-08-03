n, k = list(map(int, input().split()))

ans = 0
if k == 0:
    ans = n * n
else:
    for b in range(k + 1, n + 1):
        p = n // b
        ans += (b - k) * p
        r = n % b
        if r >= k:
            ans += r - k + 1
print(ans)
