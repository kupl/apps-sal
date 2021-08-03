
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def cross(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1


def line_intersection(line1, line2):
    px, py, qx, qy = line1
    rx, ry, sx, sy = line2

    xdiff = (px - qx, rx - sx)
    ydiff = (py - qy, ry - sy)

    div = cross(px - qx, rx - sx, py - qy, ry - sy)
    if div == 0:
        raise Exception('lines do not intersect')

    pq, rs = cross(px, py, qx, qy), cross(rx, ry, sx, sy)
    x = cross(pq, rs, px - qx, rx - sx) / div
    y = cross(pq, rs, py - qy, ry - sy) / div
    return x, y


def online(line, x, y):
    a, b, c, d = line
    if min(a, c) <= x <= max(a, c) and min(b, d) <= y <= max(b, d):
        return True
    else:
        return False


def CF1036E():
    N = int(input())
    lines = []
    count = 0
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        points = gcd(abs(x1 - x2), abs(y1 - y2)) + 1
        count += points
        lines.append((x1, y1, x2, y2))
    for i in range(N):
        d = set()
        for j in range(i + 1, N):
            px = lines[i][0]
            py = lines[i][1]
            qx = lines[j][0]
            qy = lines[j][1]
            rx = lines[i][2] - lines[i][0]
            ry = lines[i][3] - lines[i][1]
            sx = lines[j][2] - lines[j][0]
            sy = lines[j][3] - lines[j][1]

            rs = cross(rx, ry, sx, sy)
            # qpr = cross(qx - px, qy - py, rx, ry)

            if rs == 0:
                continue

            # qpr = cross(qx - px, qy - py, rx, ry)
            # qps = cross(qx - px, qy - py, sx, sy)
            # t = qps / rs
            # u = qpr / rs
            x, y = line_intersection(lines[i], lines[j])
            if not (x % 1 == 0 and y % 1 == 0):
                continue
            if not (online(lines[i], x, y) and online(lines[j], x, y)):
                continue
            d.add((x, y))

        count = count - len(d)

    return int(count)


def __starting_point():
    res = CF1036E()
    print(res)


__starting_point()
