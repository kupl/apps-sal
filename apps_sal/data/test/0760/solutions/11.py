s, r = input(), int(input())


def compare(a, b):
    return a[:len(b)] == b


def f(s, n, N):
    if not s or n < 2 * N:
        return N
    for i in range(n // 2, 0, -1):
        if compare(s[:i], s[i:2 * i]):
            return f(s[1:], n - 1, max(i, N))
    return f(s[1:], n - 1, N)


if len(s) < r:
    print((len(s) + r) // 2 * 2)
else:
    print(2 * f(s, len(s) + r, 0))
