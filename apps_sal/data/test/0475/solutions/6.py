def fact(n):
    q = 1
    for i in range(1, n + 1):
        q *= i
    return q


n, m, k = input().split()
n = int(n)
m = int(m)
k = int(k)
com = fact(n - 1) // (fact(k) * fact(n - 1 - k))
dd = m * ((m - 1)**k)
print((com * dd) % 998244353)
