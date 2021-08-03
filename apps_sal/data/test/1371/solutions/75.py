def abc178_d():
    def combi_mod_prime(n, k, p):
        ''' nCk % p (pは素数) '''
        a = 1
        b = 1
        for i in range(k):
            a = a * (n - i) % p
            b = b * (i + 1) % p
        return a * pow(b, p - 2, p) % p

    s = int(input())
    mod = 10**9 + 7
    ans = 0
    for k in range(1, s // 3 + 1):
        x = s - (3 * k)
        ans += combi_mod_prime(x + k - 1, k - 1, mod)
        ans %= mod
    print(ans)


def __starting_point():
    abc178_d()


__starting_point()
