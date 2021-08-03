N, X, M = map(int, input().split())


def calc(n, x, m):
    def nxt(y): return y**2 % m

    y = x
    r = n
    l = [0] * m
    for i in range(1, n + 1):
        if l[y]:
            r = i - l[y]
            break
        l[y] = i
        y = nxt(y)
    else:
        return sum(i for i, v in enumerate(l) if v)

    ans = 0
    for i in range(i):
        ans += x
        x = nxt(x)
    n -= i + 1
    for i in range(r):
        ans += x * (n // r)
        x = nxt(x)
    for i in range(n % r):
        ans += x
        x = nxt(x)

    return ans


print(calc(N, X, M))
