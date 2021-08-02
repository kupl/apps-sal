n = int(input())
a = list(map(str, input().split()))
mod = 998244353
ans = 0
for i in range(n):
    for j in range(len(a[i])):
        ans += int(a[i][len(a[i]) - j - 1]) * (10**(2 * j) + 10**(2 * j + 1))
        ans %= mod
print(ans * n % mod)
