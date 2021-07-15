def area(xmin, ymin, xmax, ymax):
    dx = xmax - xmin
    dy = ymax - ymin
    if (dx >= 0) and (dy >= 0):
        return dx * dy
    else:
        return 0

def intersect(a_xmin, a_ymin, a_xmax, a_ymax,
            b_xmin, b_ymin, b_xmax, b_ymax):
    xmax, xmin = min(a_xmax, b_xmax), max(a_xmin, b_xmin)
    ymax, ymin = min(a_ymax, b_ymax), max(a_ymin, b_ymin)
    return xmin, ymin, xmax, ymax    

a_xmin, a_ymin, a_xmax, a_ymax = list(map(int, input().split()))
b_xmin, b_ymin, b_xmax, b_ymax = list(map(int, input().split()))
c_xmin, c_ymin, c_xmax, c_ymax = list(map(int, input().split()))

s1 = (a_xmax - a_xmin) * (a_ymax - a_ymin)
s12_xmin, s12_ymin, s12_xmax, s12_ymax = intersect(
    a_xmin, a_ymin, a_xmax, a_ymax,
    b_xmin, b_ymin, b_xmax, b_ymax
)
s12 = area(s12_xmin, s12_ymin, s12_xmax, s12_ymax)

s13_xmin, s13_ymin, s13_xmax, s13_ymax = intersect(
    a_xmin, a_ymin, a_xmax, a_ymax,
    c_xmin, c_ymin, c_xmax, c_ymax
)
s13 = area(s13_xmin, s13_ymin, s13_xmax, s13_ymax)


s23_xmin, s23_ymin, s23_xmax, s23_ymax = intersect(
    b_xmin, b_ymin, b_xmax, b_ymax,
    c_xmin, c_ymin, c_xmax, c_ymax
)
s23 = area(s23_xmin, s23_ymin, s23_xmax, s23_ymax)

s123_xmin, s123_ymin, s123_xmax, s123_ymax = intersect(
    s13_xmin, s13_ymin, s13_xmax, s13_ymax,
    s23_xmin, s23_ymin, s23_xmax, s23_ymax
)
s123 = area(s123_xmin, s123_ymin, s123_xmax, s123_ymax)

print("YES" if s1 > s12 + s13 - s123 else "NO")
