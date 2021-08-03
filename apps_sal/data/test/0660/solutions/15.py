def read():
    return [int(s) for s in input().split()]


(n, b, p) = read()
print((n - 1) * (2 * b + 1), n * p)
