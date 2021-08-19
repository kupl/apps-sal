(n, k) = map(int, input().split())
ans = 0
if k != 0:
    for i in range(k + 1, n + 1):
        ans += n // i * (i - k)
        num = n // i * i
        ans += max(0, n - num - k + 1)
else:
    ans = n ** 2
print(ans)
