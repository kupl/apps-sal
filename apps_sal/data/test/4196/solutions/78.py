from math import gcd


class SegTree:

    def segfunc(self, x, y):
        return gcd(x, y)

    def __init__(self, ide, init_val):
        n = len(init_val)
        self.ide_ele = ide
        self.num = 2 ** (n - 1).bit_length()
        self.seg = [self.ide_ele] * 2 * self.num
        for i in range(n):
            self.seg[i + self.num - 1] = init_val[i]
        for i in range(self.num - 2, -1, -1):
            self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2])

    def update(self, idx, val):
        idx += self.num - 1
        self.seg[idx] = val
        while idx:
            idx = (idx - 1) // 2
            self.seg[idx] = self.segfunc(self.seg[idx * 2 + 1], self.seg[idx * 2 + 2])

    def query(self, begin, end):
        if end <= begin:
            return self.ide_ele
        begin += self.num - 1
        end += self.num - 2
        res = self.ide_ele
        while begin + 1 < end:
            if begin & 1 == 0:
                res = self.segfunc(res, self.seg[begin])
            if end & 1 == 1:
                res = self.segfunc(res, self.seg[end])
                end -= 1
            begin = begin // 2
            end = (end - 1) // 2
        if begin == end:
            res = self.segfunc(res, self.seg[begin])
        else:
            res = self.segfunc(self.segfunc(res, self.seg[begin]), self.seg[end])
        return res


def main():
    n = int(input())
    a = list(map(int, input().split()))
    seg = SegTree(0, a)
    ans = 1
    for i in range(n):
        ans = max(ans, gcd(seg.query(0, i), seg.query(i + 1, n)))
    print(ans)


def __starting_point():
    main()


__starting_point()
