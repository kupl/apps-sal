
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def isPrimeMR(n):
    d = n - 1
    d = d // (d & -d)
    L = [2, 7, 61] if n < 1 << 32 else [2, 3, 5, 7, 11, 13, 17] if n < 1 << 48 else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in L:
        t = d
        y = pow(a, t, n)
        if y == 1:
            continue
        while y != n - 1:
            y = y * y % n
            if y == 1 or t == n - 1:
                return 0
            t <<= 1
    return 1


def findFactorRho(n):
    m = 1 << n.bit_length() // 8
    for c in range(1, 99):
        def f(x): return (x * x + c) % n
        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for i in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for i in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x - ys), n)
        if g < n:
            if isPrimeMR(g):
                return g
            elif isPrimeMR(n // g):
                return n // g
            return findFactorRho(g)


def primeFactor(n):
    i = 2
    ret = {}
    rhoFlg = 0
    while i * i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k:
            ret[i] = k
        i += i % 2 + (3 if i % 3 == 1 else 1)
        if i == 101 and n >= 2 ** 20:
            while n > 1:
                if isPrimeMR(n):
                    ret[n], n = 1, 1
                else:
                    rhoFlg = 1
                    j = findFactorRho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                    ret[j] = k

    if n > 1:
        ret[n] = 1
    if rhoFlg:
        ret = {x: ret[x] for x in sorted(ret)}
    return ret


def divisors(pf):
    ret = [1]
    for p in pf:
        ret_prev = ret
        ret = []
        for i in range(pf[p] + 1):
            for r in ret_prev:
                ret.append(r * (p ** i))
    return sorted(ret)


T = int(input())
for _ in range(T):
    N = int(input())
    pf = primeFactor(N)
    dv = divisors(pf)
    if len(pf) == 2 and len(dv) == 4:
        print(*dv[1:])
        print(1)
        continue

    if len(pf) == 1:
        print(*dv[1:])
        print(0)
        continue

    lpf = list(pf)

    X = [[] for _ in range(len(pf))]
    S = {1}
    if len(lpf) == 2:
        X[0].append(lpf[0] * lpf[1])
        X[1].append(N)
        S.add(lpf[0] * lpf[1])
        S.add(N)
        for i, p in enumerate(lpf):
            for j in range(1, pf[p] + 1):
                X[i].append(p ** j)
                S.add(p ** j)
    else:
        for i, p in enumerate(lpf):
            X[i].append(lpf[i - 1] * p)
            S.add(lpf[i - 1] * p)
            for j in range(1, pf[p] + 1):
                X[i].append(p ** j)
                S.add(p ** j)
    for a in dv:
        if a not in S:
            for i, p in enumerate(lpf):
                if a % p == 0:
                    X[i].append(a)
                    break
    ANS = []
    for x in X:
        for y in x:
            ANS.append(y)
    print(*ANS)
    print(0)
