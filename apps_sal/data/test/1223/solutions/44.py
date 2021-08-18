from bisect import bisect_left, bisect_right, insort_right


class CubeSkipList:
    def __init__(self, values=None, sorted_=False, cube=100, seed=42):
        inf = float("inf")
        self.rand_y = seed
        self.cube = cube
        if values is None:
            self.layer2 = [inf]
            self.layer1 = [[]]
            self.layer0 = [[[]]]
        else:
            self.layer2 = layer2 = []
            self.layer1 = layer1 = []
            self.layer0 = layer0 = []
            if not sorted_:
                values.sort()
            rand_depth = self.rand_depth
            l1 = []
            la0 = []
            l0 = []
            for v in values:
                r = rand_depth()
                if r == 0:
                    l0.append(v)
                elif r == 1:
                    la0.append(l0)
                    l0 = []
                    l1.append(v)
                else:
                    la0.append(l0)
                    layer0.append(la0)
                    layer1.append(l1)
                    l0 = []
                    la0 = []
                    l1 = []
                    layer2.append(v)
            la0.append(l0)
            layer0.append(la0)
            layer1.append(l1)
            layer2.append(inf)

    def rand_depth(self):
        y = self.rand_y
        y ^= y << 13 & 0xffffffff
        y ^= y >> 17
        y ^= y << 5 & 0xffffffff
        self.rand_y = y
        if y % self.cube == 0:
            if y % (self.cube ** 2) == 0:
                return 2
            return 1
        return 0

    def add(self, x):
        layer2, layer1, layer0 = self.layer2, self.layer1, self.layer0
        r = self.rand_depth()
        if r == 0:
            idx2 = bisect_right(layer2, x)
            idx1 = bisect_right(layer1[idx2], x)
            insort_right(layer0[idx2][idx1], x)
        elif r == 1:
            idx2 = bisect_right(layer2, x)
            l1 = layer1[idx2]
            idx1 = bisect_right(l1, x)
            l1.insert(idx1, x)
            la0 = layer0[idx2]
            l0 = la0[idx1]
            idx0 = bisect_right(l0, x)

            la0.insert(idx1 + 1, l0[idx0:])
            del l0[idx0:]
        else:
            idx2 = bisect_right(layer2, x)
            layer2.insert(idx2, x)
            l1 = layer1[idx2]
            idx1 = bisect_right(l1, x)
            la0 = layer0[idx2]
            l0 = la0[idx1]
            idx0 = bisect_right(l0, x)

            la0.insert(idx1 + 1, l0[idx0:])
            del l0[idx0:]
            layer0.insert(idx2 + 1, la0[idx1 + 1:])
            del la0[idx1 + 1:]
            layer1.insert(idx2 + 1, l1[idx1:])
            del l1[idx1:]

    def remove(self, x):
        raise NotImplementedError
        layer1, layer0 = self.layer1, self.layer0
        idx1 = bisect_left(layer1, x)
        if layer1[idx1] == x:
            del layer1[idx1]
            layer0[idx1] += layer0[idx1 + 1]
            del layer0[idx1 + 1]
        else:
            layer0_idx1 = layer0[idx1]
            del layer0_idx1[bisect_left(layer0_idx1, x)]

    def bisect_left(self, x):
        raise NotImplementedError
        layer1, layer0 = self.layer1, self.layer0
        idx1 = bisect_left(layer1, x)
        res = layer1[idx1]
        if res == x:
            return res
        layer0_idx1 = layer0[idx1]
        if layer0_idx1:
            idx0 = bisect_left(layer0_idx1, x)
            if idx0 == len(layer0_idx1):
                return res
            else:
                return layer0_idx1[idx0]
        else:
            return res

    def search_higher(self, x):
        layer2, layer1, layer0 = self.layer2, self.layer1, self.layer0
        idx2 = bisect_right(layer2, x)
        l1 = layer1[idx2]
        idx1 = bisect_right(l1, x)
        la0 = layer0[idx2]
        l0 = la0[idx1]
        idx0 = bisect_right(l0, x)
        if idx0 == len(l0):
            if idx1 == len(l1):
                return layer2[idx2]
            return l1[idx1]
        return l0[idx0]

    def search_lower(self, x):
        layer2, layer1, layer0 = self.layer2, self.layer1, self.layer0
        idx2 = bisect_left(layer2, x)
        l1 = layer1[idx2]
        idx1 = bisect_left(l1, x)
        la0 = layer0[idx2]
        l0 = la0[idx1]
        idx0 = bisect_left(l0, x)
        if idx0 == 0:
            if idx1 == 0:
                return layer2[idx2 - 1]
            return l1[idx1 - 1]
        return l0[idx0 - 1]

    def pop(self, idx):
        raise NotImplementedError
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
        print(self.layer2)
        print(self.layer1)
        print(self.layer0)


def main():
    n = int(input())
    p = list(map(int, input().split()))
    idx = [0] * n
    for i in range(0, n):
        idx[i] = i
    idx.sort(key=lambda i: - p[i])
    ssl = CubeSkipList()
    ssl.add(-1)
    ssl.add(n)
    ans = 0
    for i in idx:
        nex = ssl.search_higher(i)
        nexnex = ssl.search_higher(nex)
        pre = ssl.search_lower(i)
        prepre = ssl.search_lower(pre)
        if prepre != float("inf"):
            ans += p[i] * (pre - prepre) * (nex - i)
        if nexnex != float("inf"):
            ans += p[i] * (i - pre) * (nexnex - nex)
        ssl.add(i)
    print(ans)


main()
