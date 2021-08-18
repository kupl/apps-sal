from bisect import bisect_left, bisect_right, insort_right


class SquareSkipList:
    def __init__(self, values=None, sorted_=False, square=1000, seed=1000000007):
        inf = float("inf")
        self.rand_y = seed
        self.square = square
        if values is None:
            self.layer1 = [inf]
            self.layer0 = [[]]
        else:
            self.layer1 = layer1 = []
            self.layer0 = layer0 = []
            if not sorted_:
                values.sort()
            y = seed
            l0 = []
            for v in values:
                y = self.rand_y
                y ^= y << 13 & 0xffffffff
                y ^= y >> 17
                y ^= y << 5 & 0xffffffff
                self.rand_y = y
                if y % square == 0:
                    layer0.append(l0)
                    l0 = []
                    layer1.append(v)
                else:
                    l0.append(v)
            layer1.append(inf)
            layer0.append(l0)
            self.rand_y = y

    def add(self, x):
        layer1, layer0 = self.layer1, self.layer0

        y = self.rand_y
        y ^= y << 13 & 0xffffffff
        y ^= y >> 17
        y ^= y << 5 & 0xffffffff
        self.rand_y = y

        if y % self.square == 0:
            idx1 = bisect_right(layer1, x)
            layer1.insert(idx1, x)
            layer0_idx1 = layer0[idx1]
            idx0 = bisect_right(layer0_idx1, x)
            layer0.insert(idx1 + 1, layer0_idx1[idx0:])
            del layer0_idx1[idx0:]
        else:
            idx1 = bisect_right(layer1, x)
            insort_right(layer0[idx1], x)

    def remove(self, x):
        layer1, layer0 = self.layer1, self.layer0
        idx1 = bisect_left(layer1, x)
        layer0_idx1 = layer0[idx1]
        idx0 = bisect_left(layer0_idx1, x)
        if idx0 == len(layer0_idx1):
            del layer1[idx1]
            layer0[idx1] += layer0.pop(idx1 + 1)
        else:
            del layer0_idx1[idx0]

    def search_higher_equal(self, x):
        layer1, layer0 = self.layer1, self.layer0
        idx1 = bisect_left(layer1, x)
        layer0_idx1 = layer0[idx1]
        idx0 = bisect_left(layer0_idx1, x)
        if idx0 == len(layer0_idx1):
            return layer1[idx1]
        return layer0_idx1[idx0]

    def search_higher(self, x):
        layer1, layer0 = self.layer1, self.layer0
        idx1 = bisect_right(layer1, x)
        layer0_idx1 = layer0[idx1]
        idx0 = bisect_right(layer0_idx1, x)
        if idx0 == len(layer0_idx1):
            return layer1[idx1]
        return layer0_idx1[idx0]

    def search_lower(self, x):
        layer1, layer0 = self.layer1, self.layer0
        idx1 = bisect_left(layer1, x)
        layer0_idx1 = layer0[idx1]
        idx0 = bisect_left(layer0_idx1, x)
        if idx0 == 0:
            return layer1[idx1 - 1]
        return layer0_idx1[idx0 - 1]

    def pop(self, idx):
        layer1, layer0 = self.layer1, self.layer0
        s = -1
        for i, l0 in enumerate(layer0):
            s += len(l0) + 1
            if s >= idx:
                break
        if s == idx:
            layer0[i] += layer0[i + 1]
            del layer0[i + 1]
            return layer1.pop(i)
        else:
            return layer0[i].pop(idx - s)

    def print(self):
        print(self.layer1)
        print(self.layer0)


def main():
    inf = float("inf")
    n = int(input())
    p = list(map(int, input().split()))
    idx = [0] * n
    for i in range(0, n):
        idx[i] = i
    idx.sort(key=lambda i: - p[i])
    ssl = SquareSkipList()
    ssl.add(-1)
    ssl.add(n)
    ans = 0
    for i in idx:
        nex = ssl.search_higher(i)
        nexnex = ssl.search_higher(nex)
        pre = ssl.search_lower(i)
        prepre = ssl.search_lower(pre)
        if prepre != inf:
            ans += p[i] * (pre - prepre) * (nex - i)
        if nexnex != inf:
            ans += p[i] * (i - pre) * (nexnex - nex)
        ssl.add(i)
    print(ans)


main()
