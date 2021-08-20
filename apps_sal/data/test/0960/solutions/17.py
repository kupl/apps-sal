(n, k) = map(int, input().split())
ans = 2 * 10 ** 9
i = 1
while i * i <= n:
    if n % i == 0:
        if i < k:
            ans = min(ans, i + n // i * k)
        if n // i < k:
            ans = min(ans, n // i + i * k)
    i += 1
print(ans)
