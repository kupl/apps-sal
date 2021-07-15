Z = 998244353


def ncr(n, r):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % Z
        den = (den * (i + 1)) % Z

    return (num * pow(den, Z - 2, Z)) % Z


n, m, k = list(map(int, input().split()))

print((ncr(n - 1, k) * m * pow(m - 1, k, Z)) % Z)

