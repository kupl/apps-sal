'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C
Code, Compile, Run and Debug online from anywhere in world.

'''


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def cross(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1


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
        count += gcd(abs(x1 - x2), abs(y1 - y2)) + 1
        lines.append((x1, y1, x2, y2))

    for i in range(N):
        d = set()
        for j in range(i + 1, N):
            px, py, qx, qy = lines[i]
            rx, ry, sx, sy = lines[j]

            line1p = (px - qx, rx - sx)
            line2p = (py - qy, ry - sy)

            area = cross(line1p[0], line1p[1], line2p[0], line2p[1])

            if area == 0:
                continue

            lineA = cross(px, py, qx, qy)
            lineB = cross(rx, ry, sx, sy)
            x = cross(lineA, lineB, line1p[0], line1p[1]) / area
            y = cross(lineA, lineB, line2p[0], line2p[1]) / area

            if not (x % 1 == 0 and y % 1 == 0):
                continue
            if not (online(lines[i], x, y) and online(lines[j], x, y)):
                continue

            d.add((x, y))

        count -= len(d)

    return count


def __starting_point():
    res = CF1036E()
    print(res)


__starting_point()
