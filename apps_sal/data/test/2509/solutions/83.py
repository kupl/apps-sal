(n, k) = map(int, input().split())
if k == 0:
    print(n ** 2)
else:
    ans = 0
    for b in range(k, n + 1):
        ans += n // b * (b - k)
        if n % b >= k:
            ans += n % b - (k - 1)
    print(ans)
