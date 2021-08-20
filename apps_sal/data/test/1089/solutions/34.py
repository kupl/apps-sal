(n, m, k) = map(int, input().split())
mod = 10 ** 9 + 7
kaidan = [1] * (n * m + 1)
gyaku = [1] * (n * m + 1)
for i in range(1, n * m + 1):
    kaidan[i] = i * kaidan[i - 1] % mod
    gyaku[i] = pow(kaidan[i], mod - 2, mod)


def comb(n, r):
    if n - r > 0 and n > 0 and (r > 0):
        return kaidan[n] * gyaku[n - r] * gyaku[r] % mod
    elif n == 0 or r == 0 or n == r:
        return 1
    else:
        0


ans = 0
for d in range(1, n):
    ans += d * (n - d) * m * m * comb(n * m - 2, k - 2)
for d in range(1, m):
    ans += d * (m - d) * n * n * comb(n * m - 2, k - 2)
print(ans % mod)
