def pow_mod(x, y, p):
    number = 1
    while y:
        if y & 1:
            number = number * x % p
        y >>= 1
        x = x * x % p
    return number % p


def inv(x, p):
    if 1 < x:
        return p - inv(p % x, x) * p // x
    return 1


def v(p, a, b, k):
    i = 1
    while (pow_mod(a, k, (10 ** 9 + 9) ** i) - pow_mod(b, k, (10 ** 9 + 9) ** i)) == 0:
        i += 1
    return i - 1


def main():
    p = 10 ** 9 + 9
    n, a, b, k = list(map(int, input().split()))
    S = list(input())
    for i in range(k):
        if S[i] == '+':
            S[i] = 1
        else:
            S[i] = -1
    s = 0
    if a != b:
        vp = p ** v(p, a, b, k)
        sum_mod = ((pow_mod(a, (n + 1), p * vp) - pow_mod(b, (n + 1), p * vp)) // vp) * inv(((pow_mod(a, k, p * vp) - pow_mod(b, k, p * vp)) // vp) % p, p)
        pa = pow_mod(a, k - 1, p)
        pb = 1
        inv_a = inv(a, p)
        for i in range(k):
            s += (S[i] * pa * pb * sum_mod) % p
            pa = (pa * inv_a) % p
            pb = (pb * b) % p
    else:
        for i in range(k):
            s += S[i] * (n + 1) // k
        s *= pow_mod(a, n, p)
    s %= p
    print(s)


main()
