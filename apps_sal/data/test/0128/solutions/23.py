n, k = list(map(int, input().split()))
k = min(k, n // 2)
ans = 0
for i in range(1, k + 1):
    ans += (n - i)
t = ans

ans += ((n - 2 * k) * k)

print(ans + (k * (k - 1) // 2))

