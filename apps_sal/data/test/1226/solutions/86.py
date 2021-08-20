(n, a, b) = map(int, input().split())
mod = 10 ** 9 + 7


def combi(n, r):
    (x, y) = (1, 1)
    for i in range(n - r + 1, n + 1):
        x *= i
        x %= mod
    for j in range(1, r + 1):
        y *= j
        y %= mod
    yinv = pow(y, mod - 2, mod)
    return x * yinv % mod


def main():
    nca = combi(n, a)
    ncb = combi(n, b)
    ans = pow(2, n, mod) - 1 - (nca + ncb)
    print(ans % mod)


main()
