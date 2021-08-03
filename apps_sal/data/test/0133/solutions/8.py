n, m = map(int, input().split())

mod = 10 ** 9 + 7


def binpow(a, n):
    if n == 0:
        return 1
    ans = binpow(a, n // 2)
    ans = ans * ans
    if n % 2 == 1:
        ans = ans * a
    ans = ans % mod
    return ans


print(binpow((binpow(2, m) - 1), n))
