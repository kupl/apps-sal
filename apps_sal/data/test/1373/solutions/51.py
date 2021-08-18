
n, k = list(map(int, input().split()))
mod = 10**9 + 7

ans = 1
for i in range(k, n + 1):
    min_s = i * (i - 1) // 2
    max_s = i * (2 * (n + 1 - i) + (i - 1)) // 2
    ans += max_s - min_s + 1
    ans %= mod
print(ans)
