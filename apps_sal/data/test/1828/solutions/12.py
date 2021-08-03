3


class StdIO:
    def read_int(self):
        return int(self.read_string())

    def read_ints(self, sep=None):
        return [int(i) for i in self.read_strings(sep)]

    def read_float(self):
        return float(self.read_string())

    def read_floats(self, sep=None):
        return [float(i) for i in self.read_strings(sep)]

    def read_string(self):
        return input()

    def read_strings(self, sep=None):
        return self.read_string().split(sep)


io = StdIO()


def left(u, v):
    ux, uy = u
    vx, vy = v

    z = ux * vy - uy * vx

    return z > 0


def main():
    n = io.read_int()

    x0, y0 = io.read_ints()
    x1, y1 = io.read_ints()

    pv = (x1 - x0, y1 - y0)
    ppx, ppy = x1, y1

    dang = 0
    for i in range(2, n + 1):
        px, py = io.read_ints()
        v = (px - ppx, py - ppy)

        if left(pv, v):
            dang += 1

        pv = v
        ppx, ppy = px, py

    print(dang)


def __starting_point():
    main()


__starting_point()
