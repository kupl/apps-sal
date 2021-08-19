def solve():
    (x, k, d) = map(int, input().split())
    x = abs(x)
    a = x // d
    b = x % d
    p = x - d * k
    if p > b:
        print(p)
        return
    q = x - a * d
    if (k - a) % 2 == 0:
        print(abs(q))
    else:
        print(abs(q - d))


solve()
