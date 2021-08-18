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


def main():
    n, m = io.read_ints()
    a = io.read_ints()
    a.sort()

    has = set()
    for ai in a:
        has.add(ai)

    t = []

    mu = 0
    for i in range(1, a[0]):
        if mu + i > m:
            break

        t.append(i)
        mu += i

    for i in range(a[0], a[-1]):
        if mu + i > m:
            break

        if i not in has:
            t.append(i)
            mu += i

    for i in range(a[-1] + 1, 10**9):
        if mu + i > m:
            break

        t.append(i)
        mu += i

    print(len(t))
    for ti in t:
        print(ti, end=' ')


def __starting_point():
    main()


__starting_point()
