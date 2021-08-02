n, k = map(int, input().split())
mod = 10**9 + 7

ans = 0
for i in range(k, n + 2):
    ans += n * i - i * (i - 1) + 1
    ans %= mod
print(ans)
