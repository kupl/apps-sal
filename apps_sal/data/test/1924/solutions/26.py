def solve():
    (r1, c1, r2, c2) = map(int, input().split())
    p = 10 ** 9 + 7
    N = r2 + c2 + 2
    fact = [1, 1]
    for i in range(2, N + 1):
        fact.append(fact[-1] * i % p)

    def comb(n, r):
        a = fact[n]
        b = pow(fact[r], p - 2, p)
        c = pow(fact[n - r], p - 2, p)
        return a * b * c % p

    def f(i, j):
        return comb(i + j, i)

    def g(i, j):
        return f(i + 1, j + 1) - 1
    ans = g(r2, c2) - g(r2, c1 - 1) - g(r1 - 1, c2) + g(r1 - 1, c1 - 1)
    print(ans % p)


solve()
