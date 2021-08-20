memo = [0] * (10 ** 6 + 1)
memo[0] = memo[1] = 1
mod = 10 ** 9 + 7
for i in range(2, 10 ** 6 + 1):
    memo[i] = memo[i - 1] * i % mod


def comb(n, k, p):
    return memo[n] * pow(memo[k], p - 2, p) * pow(memo[n - k], p - 2, p) % mod


(h, w, a, b) = map(int, input().split())
ans = 0
for i in range(h - a):
    ans += comb(b + i - 1, i, mod) * comb(h - i - 1 + w - b - 1, w - b - 1, mod) % mod
    ans %= mod
print(ans)
