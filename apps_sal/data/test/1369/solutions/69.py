def calc_intersection(z1, z2, R):
    d2 = (z1[0] - z2[0])**2 + (z1[1] - z2[1])**2
    d = d2 ** 0.5
    if R < d / 2:
        return None
    else:
        m = [(z1[0] + z2[0]) * 0.5, (z1[1] + z2[1]) * 0.5]
        l = (R**2 / d2 - 0.25)**0.5
        v = [l * (z2[1] - z1[1]), l * (z1[0] - z2[0])]
        return [[m[0] + v[0], m[1] + v[1]], [m[0] - v[0], m[1] - v[1]]]


def check(R):
    intersections = []
    for i in range(N):
        for j in range(i + 1, N):
            points = calc_intersection(xy[i], xy[j], R)
            if points is None:
                return False
            else:
                intersections.extend(points)

    for px, py in intersections:
        res = True
        for x, y in xy:
            res *= ((x - px)**2 + (y - py)**2 <= R**2 + 0.000001)
            if not res:
                break
        if res:
            return True
    return False


N = int(input())
xy = [list(map(int, input().split())) for i in range(N)]
left = 0
right = 500 * 2**0.5
while right - left > 0.000001:
    mid = (left + right) / 2
    if check(mid):
        right = mid
    else:
        left = mid

print(right)
