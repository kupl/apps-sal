def main():
    M = 10 ** 9 + 7
    (a, b, c, d) = map(int, input().split())
    n = c + d + 2
    fac = [0] * (n + 1)
    fac[0] = lt = 1
    for i in range(1, n + 1):
        fac[i] = lt = lt * i % M

    def inv(n):
        return pow(fac[n], M - 2, M)

    def f(r, c):
        return fac[r + c + 2] * inv(c + 1) * inv(r + 1) - c - r - 2
    print((f(c, d) - f(c, b - 1) - f(a - 1, d) + f(a - 1, b - 1)) % M)


main()
