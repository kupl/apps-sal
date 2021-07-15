def min_disc(points):
    from random import sample
    N = len(points)
    if N == 1:
        return points[0], 0
    points = sample(points, N)
    def cross(a, b):
        return a.real * b.imag - a.imag * b.real
    def norm2(a):
        return a.real * a.real + a.imag * a.imag
    def make_circle_3(a, b, c):
        A, B, C = norm2(b-c), norm2(c-a), norm2(a-b)
        S = cross(b-a, c-a)
        p = (A*(B+C-A)*a + B*(C+A-B)*b + C*(A+B-C)*c) / (4*S*S)
        radius = abs(p-a)
        return p, radius
    def make_circle_2(a, b):
        c = (a+b) / 2
        radius = abs(a-c)
        return c, radius
    def in_circle(point, circle):
        return abs(point-circle[0]) <= circle[1]+1e-7
    p0 = points[0]
    circle = make_circle_2(p0, points[1])
    for i, p_i in enumerate(points[2:], 2):
        if not in_circle(p_i, circle):
            circle = make_circle_2(p0, p_i)
            for j, p_j in enumerate(points[1:i], 1):
                if not in_circle(p_j, circle):
                    circle = make_circle_2(p_i, p_j)
                    for p_k in points[:j]:
                        if not in_circle(p_k, circle):
                            circle = make_circle_3(p_i, p_j, p_k)
    return circle

N = int(input())
XY = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    XY.append(x + y*1j)
center, rad = min_disc(XY)
print(rad)

