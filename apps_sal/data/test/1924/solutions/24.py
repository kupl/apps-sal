def main():
    mod = 10 ** 9 + 7
    fact = [1, 1]
    for i in range(2, 2 * 10 ** 6 + 10):
        fact.append(fact[-1] * i % mod)
    (r1, c1, r2, c2) = map(int, input().split())
    r1 -= 1
    c1 -= 1

    def calc(r, c):
        return (pow(fact[c + 1] * fact[r + 1] % mod, mod - 2, mod) * fact[r + c + 2] - 1) % mod
    print((calc(r2, c2) - calc(r1, c2) - calc(r2, c1) + calc(r1, c1)) % mod)


main()
