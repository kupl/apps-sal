n = int(input())
mod = 10 ** 9 + 7
c = list(map(int, input().split()))
c.sort()
ans = 0
for i in range(n):
    if i < n - 1:
        ans += c[i] * (n - i + 1) * pow(2, n - i - 2, mod) * pow(2, i, mod)
        ans %= mod
    else:
        ans += c[i] * pow(2, n - i - 1, mod) * pow(2, i, mod)
        ans %= mod
ans *= pow(2, n, mod)
ans %= mod
print(ans)
