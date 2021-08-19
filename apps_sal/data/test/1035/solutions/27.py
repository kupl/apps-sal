from math import gcd


def resolve():

    def prime_factorize(n):
        if 2 <= n < 4:
            return [n]
        res = []
        i = 2
        while i * i <= n:
            while n % i == 0:
                res.append(i)
                n //= i
            i += 1
        if n != 1:
            res.append(n)
        return set(res)
    (a, b) = list(map(int, input().split()))
    g = gcd(a, b)
    ans = prime_factorize(g)
    print(len(ans) + 1)


def __starting_point():
    resolve()


__starting_point()
