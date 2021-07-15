def main():
    from math import sqrt
    n, k = list(map(int, input().split()))
    g, x = n * 2 // ((k + 1) * k), n
    if not g:
        print(-1)
        return
    divisors = [1]
    p = q = 1
    while not x % 2:
        x //= 2
        q *= 2
        divisors.append(q)
    while True:
        lim = int(sqrt(x))
        if p >= lim:
            break
        for p in range(p + 2, lim + 2, 2):
            if not x % p:
                l, q = [], 1
                while not x % p:
                    x //= p
                    q *= p
                    l.append(q)
                divisors += [p * q for p in l for q in divisors]
                break
        else:
            break
    if x != 1:
        divisors += [x * q for q in divisors]
    g = max(p for p in divisors if p <= g)
    print(' '.join(map(str, list(range(g, g * k, g)))), n - g * (k - 1) * k // 2)


def __starting_point():
    main()

__starting_point()
