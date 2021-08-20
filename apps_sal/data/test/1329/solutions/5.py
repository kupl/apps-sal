import sys
sys.setrecursionlimit(10 ** 8)


def Z():
    return int(input())


def ZZ():
    return [int(_) for _ in input().split()]


def main():
    N = Z()

    def sieve(num):
        isPrime = [True] * (num + 1)
        isPrime[0] = isPrime[1] = False
        for i in range(2, num + 1):
            if i * i > num:
                break
            if not isPrime[i]:
                continue
            for j in range(i, num + 1):
                if i * j > num:
                    break
                isPrime[i * j] = False
        return isPrime
    ps = []
    cs = []
    s = sieve(N)
    for i in range(N + 1):
        if s[i]:
            ps.append(i)
    for p in ps:
        (cc, q) = (0, p)
        while N // q > 0:
            cc += N // q
            q *= p
        cs.append(cc)
    ans = set()
    for i in range(len(cs)):
        if cs[i] >= 74:
            ans.add(pow(ps[i], 74))
    for i in range(len(cs)):
        for j in range(len(cs)):
            if i == j:
                continue
            if cs[i] >= 24 and cs[j] >= 2:
                ans.add(pow(ps[i], 24) * pow(ps[j], 2))
            if cs[i] >= 14 and cs[j] >= 4:
                ans.add(pow(ps[i], 14) * pow(ps[j], 4))
    for i in range(len(cs)):
        for j in range(len(cs)):
            for k in range(len(cs)):
                if i == j or j == k or k == i:
                    continue
                if cs[i] >= 4 and cs[j] >= 4 and (cs[k] >= 2):
                    ans.add(pow(ps[i], 4) * pow(ps[j], 4) * pow(ps[k], 2))
    print(len(ans))
    return


def __starting_point():
    main()


__starting_point()
