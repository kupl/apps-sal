def f(a):
    c, v, m = 0, 0, 1
    for i in range(len(a) - 1):
        x = m * abs(a[i] - a[i + 1])
        c = max(c + x, x)
        v = max(v, c)
        m *= -1
    return v
n, a = int(input()), list(map(int, input().split()))
print(max(f(a), f(a[1:])))
