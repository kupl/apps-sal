s = int(input())
"""
nm + (n-1)(m-1) + ...
nm + nm -(n+m) + 1
6x
= 6mn*n - 3*(n-1)n(n+m) + (n-1)*n*(2n-1)
6x - n*(n+1)*(2n+1)+3*(n-1)n*n = (6n*n - 3*(n-1)*n)*m
"""
a, b = [], []
for n in range(1, 1450000):
    u = 6 * s - n * (n - 1) * (n + n - 1) + 3 * (n - 1) * n * n
    v = 6 * n * n - 3 * (n - 1) * n
    if u % v == 0:
        u //= v
        if n <= u:
            a += [(n, u)]
            if n < u:
                b += [(u, n)]
        else:
            break
print(len(a) + len(b))
for e in a:
    print(*e)
for e in reversed(b):
    print(*e)
