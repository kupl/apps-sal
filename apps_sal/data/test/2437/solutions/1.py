key = 312
rnd_mod = 12345678901234567891
rnd_x = 9876543210987654321 + 1234567890123456789 * key % rnd_mod


def rnd():
    nonlocal rnd_x
    rnd_x = rnd_x**2 % rnd_mod
    return (rnd_x >> 10) % (1 << 40)


def randrange(a, b=-1):
    if b > 0:
        return randrange(b - a) + a
    return rnd() % a


def primeFactor(N):
    i = 2
    ret = {}
    n = N
    mrFlg = 0
    while i * i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k:
            ret[i] = k
        i += 1 + i % 2
        if i == 101 and n >= 2**20:
            def findFactorRho(N):
                def gcd(a, b):
                    while b:
                        a, b = b, a % b
                    return a

                def f(x, c):
                    return (x * x + c) % N
                for c in range(1, 99):
                    X, d, j = [2], 1, 0
                    while d == 1:
                        j += 1
                        X.append(f(X[-1], c))
                        X.append(f(X[-1], c))
                        d = gcd(abs(X[2 * j] - X[j]), N)
                    if d != N:
                        if isPrimeMR(d):
                            return d
                        elif isPrimeMR(N // d):
                            return N // d
            while n > 1:
                if isPrimeMR(n):
                    ret[n], n = 1, 1
                else:
                    mrFlg = 1
                    j = findFactorRho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                    ret[j] = k

    if n > 1:
        ret[n] = 1
    if mrFlg > 0:
        ret = {x: ret[x] for x in sorted(ret)}
    return list(ret)


def isPrimeMR(n):
    if n == 2:
        return True
    if n == 1 or n & 1 == 0:
        return False
    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    L = [2, 7, 61] if n < 1 << 32 else [2, 13, 23, 1662803] if n < 1 << 40 else [2, 3, 5, 7, 11, 13, 17] if n < 1 << 48 else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for a in L:
        t = d
        y = pow(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = (y * y) % n
            t <<= 1

        if y != n - 1 and t & 1 == 0:
            return False
    return True


N = int(input())
A = [int(a) for a in input().split()]
P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def chk(p):
    s = 0
    for a in A:
        am = a % p
        s += min(am, p - am) if a > p else p - a
    return s


mi = 1 << 100
for p in P:
    mi = min(mi, chk(p))

D = {}
for i in range(100):
    a = A[randrange(N)]
    for p in primeFactor(a - 1) + primeFactor(a) + primeFactor(a + 1):
        if p > 100:
            if p not in D:
                D[p] = 1
            else:
                D[p] += 1
X = [x[1] for x in sorted([(D[a], a) for a in D])[::-1][:20]]
for p in X:
    mi = min(mi, chk(p))

print(mi)
