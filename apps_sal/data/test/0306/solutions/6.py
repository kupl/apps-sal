def congr(a, b, p, x):
    solutions = 0
    power = pow(a, p - 2, p)
    a2, b2, s, d1 = 1, b, 0, -b
    prod = p * (p - 1)
    while s < p - 1:
        k = (d1 + s) % p
        L = x - s - (p - 1) * k
        solutions += L // prod + 1
        d1 = (d1 * power) % p
        s += 1
    return solutions


a, b, p, x = [int(j) for j in input().split()]
print(congr(a, b, p, x))

