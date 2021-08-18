3


class StdReader:
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


reader = StdReader()


def part_sort(a, i, j, reverse=False):
    a[i:j] = sorted(a[i:j], reverse=reverse)


def part_sorted(b, i, j, reverse=False):
    a = list(b)
    part_sort(a, i, j, reverse)
    return a


def main():
    n, m = reader.read_ints()
    a = reader.read_ints()

    ops = []
    for i in range(m):
        t, r = reader.read_ints()
        op = (t, r)

        while ops and op[1] >= ops[-1][1]:
            ops.pop()

        ops.append(op)

    max_r = ops[0][1]
    b = sorted(a[:max_r])
    bl = 0
    br = max_r - 1

    for i in range(len(ops)):
        t, r = ops[i]

        r1 = 0
        if i < len(ops) - 1:
            t1, r1 = ops[i + 1]

        k = r - r1

        if t == 1:
            for p in range(k):
                a[r - 1 - p] = b[br]
                br -= 1
        else:
            for p in range(k):
                a[r - 1 - p] = b[bl]
                bl += 1

    for ai in a:
        print(ai, end=' ')


def __starting_point():
    main()


__starting_point()
