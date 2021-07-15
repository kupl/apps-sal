

def main():
    n, a, b = list(map(int, input().split()))
    mod = 10 ** 9 + 7

    def cmb(n, r):
        if n - r < r: r = n - r
        if r == 0: return 1
        if r == 1: return n

        numerator = [n - r + k + 1 for k in range(r)]
        denominator = [k + 1 for k in range(r)]

        for p in range(2, r + 1):
            pivot = denominator[p - 1]
            if pivot > 1:
                offset = (n - r) % p
                for k in range(p - 1, r, p):
                    numerator[k - offset] /= pivot
                    denominator[k] /= pivot

        result = 1
        for k in range(r):
            if numerator[k] > 1:
                result *= int(numerator[k])
                result %= 10**9+7

        return result

    print((int(
        ((pow(2, n, mod) - 1) % mod
         - (cmb(n, a)) % mod
         - (cmb(n, b)) % mod)
        % mod)
    ))


main()


