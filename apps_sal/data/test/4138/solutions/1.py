def g(n):
    s = str(n)
    ans = 0
    for i in range(1, len(s)):
        ans += i * 9 * 10**(i - 1)

    return n * len(s) - (len(s) * (10**(len(s) - 1) - 1) - ans)


def sum(i, j):
    return i * (j - i + 1) + (j - i) * (j - i + 1) // 2


def f(n):
    ans = (n + 1) * g(n)
    s = str(n)
    for i in range(1, len(s)):
        ans -= i * sum(10 ** (i - 1), 10 ** i - 1)
    ans -= len(s) * sum(10 ** (len(s) - 1), n)
    return ans


def slow_g(n):
    s = ""
    for i in range(1, n + 1):
        s += str(i)

    return len(s)


def slow_f(n):
    ans = 0
    for i in range(1, n + 1):
        ans += g(i)
    return ans


def ans(n):
    l, r = 0, 10**18
    while l + 1 < r:
        m = (l + r) // 2
        if f(m) >= n:
            r = m
        else:
            l = m

    n -= f(r - 1)

    l = 0
    r = r
    while l + 1 < r:
        m = (l + r) // 2
        if g(m) >= n:
            r = m
        else:
            l = m
    n -= g(r - 1)
    return str(r)[n - 1]


q = int(input())
for i in range(q):
    n = int(input())
    print(ans(n))
