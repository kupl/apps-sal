def divisor(n):
    n2 = int(n ** 0.5 + 1)
    ret = set()
    for i in range(1, n2 + 1):
        if n % i == 0:
            ret.add(i)
            ret.add(n // i)
    ret = list(ret)
    ret.sort()
    return ret


def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


def lcm(a, b):
    return a // gcd(a, b) * b


def solve():
    inf = 1 << 60
    (a, b) = list(map(int, input().split()))
    if a > b:
        (a, b) = (b, a)
    if a == b:
        return 0
    ma = min(a, b)
    D = divisor(b - a)
    best_lcm = inf
    best_k = 0
    for d in D:
        r1 = a % d
        r2 = b % d
        if r1 == r2:
            k = 0
            if r1 != 0:
                k = d - r1
            lcm1 = lcm(a + k, b + k)
            if best_lcm > lcm1:
                best_lcm = lcm1
                best_k = k
            elif best_lcm == lcm1:
                best_k = min(best_k, k)
    return best_k


print(solve())
