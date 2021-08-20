s = int(input())
k = s // 3
ans = 0
mod = 10 ** 9 + 7
mod = 10 ** 9 + 7


def comb(x, y):
    s = 1
    t = 1
    for i in range(1, y + 1):
        s = s * (x - i + 1) % mod
        t = t * i % mod
    return s * pow(t, mod - 2, mod) % mod


for i in range(1, k + 1):
    ans += comb(s - 3 * i + i - 1, i - 1)
    ans %= mod
print(ans)
