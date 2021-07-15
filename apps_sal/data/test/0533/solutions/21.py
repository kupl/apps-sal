a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())

def mn(a1, a2, k1, k2, n):
    n -= (k1 - 1) * a1 + (k2 - 1) * a2
    if n <= 0:
        return 0

    return min(n, a1 + a2)

def mx(a1, a2, k1, k2, n):
    if k1 > k2:
        a1, a2 = a2, a1
        k1, k2 = k2, k1

    if k1 * a1 >= n:
        return n // k1

    n -= k1 * a1

    return a1 + min(a2, n // k2)

print(mn(a1, a2, k1, k2, n), mx(a1, a2, k1, k2, n))


