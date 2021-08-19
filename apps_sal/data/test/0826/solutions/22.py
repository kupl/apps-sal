N = int(input())


def f(k):
    return (k + 1) * k // 2


def bi_re():
    l = 0
    r = N + 1
    while l <= r:
        m = (l + r) // 2
        if f(m) > N + 1:
            r = m - 1
        elif f(m) < N + 1:
            l = m + 1
        else:
            return m
    return r


k = bi_re()
print(N - k + 1)
