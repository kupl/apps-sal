def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a // gcd(a, b) * b


def isPrime(x):
    if x < 2 or x % 2 == 0:
        return False
    if x == 2:
        return True
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True


def divisor(x):
    res = []
    i = 1
    while i * i <= x:
        if x % i == 0:
            res.append(i)
            if i * i != x:
                res.append(x // i)
        i += 1
    res = sorted(res)
    return res


def factor(x):
    res = []
    if x == 1:
        res.push_back(1)
        return res
    i = 2
    while i * i <= x:
        while x % i == 0:
            res.append(i)
            x //= i
    if x != 1:
        res.append(x)
    res = sorted(res)
    return res


def __starting_point():
    (N, K) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A = sorted(A)
    sum_v = sum(A)
    div = divisor(sum_v)
    div = sorted(div, reverse=True)
    for e in div:
        ok = True
        b = [int(a % e) for a in A]
        b = sorted(b)
        v = sum(b)
        v //= e
        ans = 0
        for i in range(N - v):
            ans += b[i]
        if ans <= K:
            print(e)
            return


__starting_point()
