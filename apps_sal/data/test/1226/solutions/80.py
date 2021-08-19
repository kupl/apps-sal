import math


def main():
    n, a, b = [int(x) for x in input().split(" ")]
    # 2^n - 1 - nCa - nCb
    p = 1000000007
    a = min([a, n - a])
    b = min([b, n - b])
    M = max([a, b])
    f = [1, 1]
    finv = []
    for i in range(M):
        f.append((f[-1] * (i + 2)) % p)
    lf = len(f)
    finv.append(modpower(f[-1], p - 2, p))
    for i in range(lf - 1):
        finv.append((finv[-1] * (lf - i - 1)) % p)
    na = 1
    nb = 1
    for i in range(M):
        if a > i:
            na = (na * (n - i)) % p
        if b > i:
            nb = (nb * (n - i)) % p
    print((modpower(2, n, p) - 1 - (na * finv[lf - 1 - a]) % p - (nb * finv[lf - 1 - b]) % p) % p)


def modpower(a, p, d):  # a^p % d
    pp = [a]
    for i in range(int(math.log2(p)) + 1):
        pp.append((pp[-1] ** 2) % d)
    b_p = format(p, 'b')
    m = 1
    for i in range(len(b_p)):
        if b_p[-i - 1] == "1":
            m = (m * pp[i]) % d
    return m


main()
