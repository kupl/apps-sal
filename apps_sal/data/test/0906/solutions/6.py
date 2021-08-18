n, m, k = list(map(int, input().split()))
mod = 10 ** 9 + 7


def p(x):
    if x == 0:
        return 1
    if (x % 2 == 0):
        return (p(x // 2) ** 2) % mod
    return (p(x // 2) ** 2 * 2) % mod


if k == -1 and (n + m) % 2 == 1:
    print(0)
else:
    print(p(n * m - n - m + 1))
