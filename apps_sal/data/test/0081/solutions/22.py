(A, B) = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


def primeFactor(N):
    i = 2
    ret = {}
    n = N
    if n < 0:
        ret[-1] = 1
        n = -n
    if n == 0:
        ret[0] = 1
    d = 2
    sq = int(n ** (1 / 2))
    while i <= sq:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
            ret[i] = k
        if k > 0:
            sq = int(n ** (1 / 2))
        if i == 2:
            i = 3
        elif i == 3:
            i = 5
        elif d == 2:
            i += 2
            d = 4
        else:
            i += 4
            d = 2
    if n > 1:
        ret[n] = 1
    return ret


def divisors(N):
    pf = primeFactor(N)
    ret = [1]
    for p in pf:
        ret_prev = ret
        ret = []
        for i in range(pf[p] + 1):
            for r in ret_prev:
                ret.append(r * p ** i)
    return sorted(ret)


if A == B:
    print(0)
else:
    mi = 10 ** 100
    ans = -1
    D = divisors(abs(B - A))
    for d in D:
        k = -A % d
        L = lcm(A + k, B + k)
        if mi > L or (mi == L and ans > k):
            mi = L
            ans = k
    print(ans)
