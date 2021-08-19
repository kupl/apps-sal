from decimal import *

getcontext().prec = 40
eps = Decimal('1e-10')


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def contains(self, c):
        dd = (self.x - c.x)**2 + (self.y - c.y)**2  # dd = d*d
        return dd < (self.r - c.r)**2 and self.r > c.r

    def in_touches(self, c):
        dd = (self.x - c.x)**2 + (self.y - c.y)**2  # dd = d*d
        return dd == (self.r - c.r)**2 and self.r > c.r

    def ex_touches(self, c):
        dd = (self.x - c.x)**2 + (self.y - c.y)**2  # dd = d*d
        return dd == (self.r + c.r)**2

    def intersects(self, c):
        dd = (self.x - c.x)**2 + (self.y - c.y)**2  # dd = d*d
        return (self.r - c.r)**2 < dd < (self.r + c.r)**2

    def not_intersects(self, c):
        dd = (self.x - c.x)**2 + (self.y - c.y)**2  # dd = d*d
        return dd > (self.r + c.r)**2

    def get_intersections(self, c):
        x1, y1, r1, x2, y2, r2 = list(map(Decimal, [self.x, self.y, self.r, c.x, c.y, c.r]))

        RR = (x1 - x2)**2 + (y1 - y2)**2

        rx1 = (x1 + x2) / 2 + (r1**2 - r2**2) / (2 * RR) * (x2 - x1) + (2 * (r1**2 + r2**2) / RR - (r1**2 - r2**2)**2 / (RR**2) - 1).sqrt() / 2 * (y2 - y1)
        ry1 = (y1 + y2) / 2 + (r1**2 - r2**2) / (2 * RR) * (y2 - y1) + (2 * (r1**2 + r2**2) / RR - (r1**2 - r2**2)**2 / (RR**2) - 1).sqrt() / 2 * (x1 - x2)

        rx2 = (x1 + x2) / 2 + (r1**2 - r2**2) / (2 * RR) * (x2 - x1) - (2 * (r1**2 + r2**2) / RR - (r1**2 - r2**2)**2 / (RR**2) - 1).sqrt() / 2 * (y2 - y1)
        ry2 = (y1 + y2) / 2 + (r1**2 - r2**2) / (2 * RR) * (y2 - y1) - (2 * (r1**2 + r2**2) / RR - (r1**2 - r2**2)**2 / (RR**2) - 1).sqrt() / 2 * (x1 - x2)

        return {(rx1, ry1), (rx2, ry2)}

    def is_on(self, p):
        return abs((self.x - p[0])**2 + (self.y - p[1])**2 - self.r**2) < eps

    def __repr__(self):
        return "(%s, %s, %s)" % (self.x, self.y, self.r)


def count_regions(n, circles):
    if n == 1:
        return 2

    if n == 2:
        return 3 + circles[0].intersects(circles[1])

    if n == 3:
        c0, c1, c2 = circles
        if c0.not_intersects(c1):
            if c0.intersects(c2):
                return 5 + c1.intersects(c2)
            elif c0.ex_touches(c2) or c2.not_intersects(c0):
                return 4 + c1.intersects(c2)
            elif c0.contains(c2) or c0.in_touches(c2):
                return 4

        elif c0.contains(c1):
            if c0.in_touches(c2) or c0.contains(c2):
                return 4 + c1.intersects(c2)
            elif c0.ex_touches(c2) or c0.not_intersects(c2):
                return 4
            elif c0.intersects(c2):
                return 5 + c1.intersects(c2)

        elif c0.in_touches(c1):
            if c0.in_touches(c2):
                if c1.intersects(c2):
                    return 6
                elif c1.ex_touches(c2):
                    return 5
                else:
                    return 4
            elif c0.not_intersects(c2) or c0.ex_touches(c2):
                return 4
            elif c0.contains(c2):
                return 4 + c1.intersects(c2)
            elif c0.intersects(c2):
                if c1.intersects(c2):
                    # intersects: 7/6, depends on intersections
                    c0_x_c2 = c0.get_intersections(c2)
                    return 6 + all(not c1.is_on(p) for p in c0_x_c2)
                else:
                    return 5 + (c1.ex_touches(c2) or c2.in_touches(c1))

        elif c0.ex_touches(c1):
            if c0.in_touches(c2) or c0.contains(c2):
                return 4

            elif c0.ex_touches(c2):
                if c1.intersects(c2):
                    return 6
                elif c1.ex_touches(c2):
                    return 5
                else:
                    return 4

            elif c0.not_intersects(c2):
                return 4 + c1.intersects(c2)

            elif c0.intersects(c2):
                if c1.intersects(c2):
                    # intersects: 8/7/6?
                    c0_x_c1 = c0.get_intersections(c1)
                    return 7 + all(not c2.is_on(p) for p in c0_x_c1)
                elif c1.ex_touches(c2):
                    return 6
                else:
                    return 5

        elif c0.intersects(c1):
            if c0.not_intersects(c2):
                return 5 + c1.intersects(c2)

            elif c0.contains(c2):
                # [?] c1.intersects(c2) -> ?
                return 5 + c1.intersects(c2)

            elif c0.in_touches(c2) or c0.ex_touches(c2):
                if c1.intersects(c2):
                    c0_x_c2 = c0.get_intersections(c2)
                    return 6 + all(not c1.is_on(p) for p in c0_x_c2)
                else:
                    return 5 + (c1.in_touches(c2) or c1.ex_touches(c2))

            elif c0.intersects(c2):
                c0_x_c1 = c0.get_intersections(c1)
                if c1.intersects(c2):
                    if all(not c2.is_on(p) for p in c0_x_c1):
                        return 8
                    elif all(c2.is_on(p) for p in c0_x_c1):
                        return 6
                    else:
                        return 7

                elif c1.in_touches(c2) or c1.ex_touches(c2) or c2.in_touches(c1):
                    return 7 - any(c2.is_on(p) for p in c0_x_c1)

                else:  # if c1.contains(c2) or c2.contains(c1) or c1.not_intersects(c2):
                    return 6

        return 4

    return 0


def main():
    n = int(input())
    circles = [tuple(map(int, input().split())) for c in range(n)]
    circles.sort(key=lambda c: (-c[2], c[0], c[1]))
    circles = [Circle(*u) for u in circles]
    # print(n, circles)
    print(count_regions(n, circles))


def __starting_point():
    main()


__starting_point()
