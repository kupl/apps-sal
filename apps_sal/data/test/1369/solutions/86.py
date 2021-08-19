Point = complex
(N, *XY) = map(int, open(0).read().split())
P = [Point(x, y) for (x, y) in zip(*[iter(XY)] * 2)]


def max_distance(center):
    return max((abs(center - p) for p in P))


def g(x):
    (left, right) = (-1000, 1000)
    for _ in range(100):
        m1 = (left * 2 + right) / 3
        m2 = (left + right * 2) / 3
        if max_distance(Point(x, m1)) < max_distance(Point(x, m2)):
            right = m2
        else:
            left = m1
    return max_distance(Point(x, left))


(left, right) = (-1000, 1000)
for _ in range(100):
    m1 = (left * 2 + right) / 3
    m2 = (left + right * 2) / 3
    if g(m1) < g(m2):
        right = m2
    else:
        left = m1
print(g(left))
