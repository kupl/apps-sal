m = 10**9 + 7
n, a, b = map(int, input().split())


def c(k):
    v = 1
    w = 1
    for i in range(k):
        v = v * (n - i) % m
        w = w * (i + 1) % m
    return (v * pow(w, m - 2, m) % m)


print((pow(2, n, m) - 1 - c(a) - c(b)) % m)
