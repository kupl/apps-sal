Point = complex
(N, *XY) = map(int, open(0).read().split())
P = [Point(x, y) for (x, y) in zip(*[iter(XY)] * 2)]


def max_distance(center):
    return max((abs(center - p) for p in P))


def ternary_search(f, left, right, MAX_ITER=100):
    for _ in range(MAX_ITER):
        m1 = (left * 2 + right) / 3
        m2 = (left + right * 2) / 3
        if f(m1) < f(m2):
            right = m2
        else:
            left = m1
    return f(left)


def g(x):
    return ternary_search(lambda y: max_distance(Point(x, y)), -1000, 1000)


print(ternary_search(g, -1000, 1000))
