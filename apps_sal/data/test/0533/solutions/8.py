def mx(a1, a2, k1, k2, n):
    fst = min(n // k1, a1)
    n -= fst * k1
    scd = min(n // k2, a2)
    return fst + scd


def mn(a1, a2, k1, k2, n):
    n -= a1 * (k1 - 1) + a2 * (k2 - 1)
    return max(n, 0)


a1, a2, k1, k2, n = [int(input()) for _ in range(5)]
if k1 > k2:
    a1, a2 = a2, a1
    k1, k2 = k2, k1
print(mn(a1, a2, k1, k2, n), mx(a1, a2, k1, k2, n))

