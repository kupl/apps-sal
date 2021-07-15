def ccw(a, b, c):
    ab = (b[1]-a[1], b[0]-a[0])
    ac = (c[1]-a[1], c[0]-a[0])
    charge = (ab[0]*ac[1] - ab[1]*ac[0])
    return charge > 0
def countccw(points):
    c = 0
    for i in range(len(points)-2):
        if ccw(points[i], points[i+1], points[i+2]): c += 1
    return c
def countcw(points):
    c = 0
    for i in range(len(points)-2):
        if not ccw(points[i], points[i+1], points[i+2]): c += 1
    return c
def __starting_point():
    n = int(input())
    points = [ tuple(int(x) for x in input().split()) for i in range(n+1) ]
    if ccw(points[-3], points[-2], points[-1]):
        print(countcw(points))
    else:
        print(countccw(points))

__starting_point()
