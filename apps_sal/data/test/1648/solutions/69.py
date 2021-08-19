import sys
p = 10 ** 9 + 7


def exp(y, x):
    xbin = str(bin(x))[2:]
    ans = 1
    yl = [0] * (len(xbin) + 1)
    yl[0] = y
    yl[1] = y ** 2
    for (d, i) in enumerate(xbin[::-1], start=0):
        if d > 1:
            yl[d] = yl[d - 1] ** 2 % p
        if i == '1':
            ans = ans * yl[d] % p
    return ans % p


sys.setrecursionlimit(200000000)


def ff(n, ca):
    if ca == 0:
        return 1
    if ca == 1:
        return n
    return n * ff(n - 1, ca - 1) % p


def main():
    (n, k) = map(int, input().split())
    fact = [1, 1]
    for i in range(2, n + 1):
        fact.append(fact[-1] * i % p)
    for i in range(1, k + 1):
        t1 = ff(k - 1, i - 1) * exp(fact[i - 1], p - 2) % p
        t2 = ff(n - k + 1, i) * exp(fact[i], p - 2) % p
        print(t1 * t2 % p)


def __starting_point():
    main()


__starting_point()
