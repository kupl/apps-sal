import math
(x, y) = map(int, input().split())
mod = 10 ** 9 + 7
fac = [1, 1]
finv = [1, 1]
inv = [0, 1]


def init(n):
    for i in range(2, n + 1):
        fac.append(fac[-1] * i % mod)
        inv.append(-inv[mod % i] * (mod // i) % mod)
        finv.append(finv[-1] * inv[-1] % mod)


def com(n, k, mod):
    if n < 0 or k < 0 or n < k:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod


def main():
    if (x + y) % 3:
        print(0)
        return
    else:
        n = (2 * y - x) // 3
        m = (2 * x - y) // 3
        if n < 0 or m < 0:
            print(0)
            return
        else:
            init(n + m)
            print(com(n + m, n, mod))


main()
