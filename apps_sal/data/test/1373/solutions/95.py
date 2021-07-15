n, k = list(map(int, input().split()))
mod = 10**9 + 7

s = [0]*(n+1)
s[0] = n + 1
for i in range(1, n+1):
    s[i] = (s[i-1] + n - 2 * i) % mod

ans = 0
for i in range(k-1, n+1):
    ans += s[i]
    ans %= mod

print(ans)

