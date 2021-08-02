with open(0) as f:
    a, b, c, d = map(int, f.read().split())


def f(x): return 0 if x < 0 else x


print(f(min(b, d) - max(a, c)))
