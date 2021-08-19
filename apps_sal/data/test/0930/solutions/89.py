def main():
    import sys
    sys.setrecursionlimit(10 ** 9)
    input = sys.stdin.readline
    (n, k) = map(int, input().split())
    mod = 1000000007

    def make_fact(n):
        fact = [1] * (n + 1)
        ifact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % mod
        ifact[n] = pow(fact[n], mod - 2, mod)
        for i in range(n, 0, -1):
            ifact[i - 1] = ifact[i] * i % mod
        return (fact, ifact)
    (fact, ifact) = make_fact(n)

    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * ifact[k] * ifact[n - k] % mod
    ans = 0
    if k > n - 1:
        k = n - 1
    for i in range(k + 1):
        ans = (ans + comb(n, i) * comb(n - 1, i)) % mod
    print(ans)


main()
