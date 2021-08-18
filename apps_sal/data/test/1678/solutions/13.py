def sort_list(list1, list2):

    zipped_pairs = zip(list2, list1)

    z = [x for _, x in sorted(zipped_pairs)]

    return z


class SegmentTree:
    def __init__(self, data, default=0, func=lambda a, b: a + b):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        if start == stop:
            return self.__getitem__(start)
        stop += 1
        start += self._size
        stop += self._size

        res = self._default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


def calc(prefix, t):
    ind = [i for i in range(len(prefix))]
    ind = sort_list(ind, prefix)
    prefix.sort()
    a = [0] * len(prefix)
    s = SegmentTree(a)
    j = 0
    ans = 0
    for i in range(len(prefix)):
        if j == len(prefix):
            ans += s.query(ind[i] + 1, len(prefix) - 1)
            continue
        while(prefix[j] - t < prefix[i]):
            s.__setitem__(ind[j], 1)
            j += 1
            if j == len(prefix):
                break
        ans += s.query(ind[i] + 1, len(prefix) - 1)
    print(ans)


n, t = map(int, input().split())
l = list(map(int, input().split()))
pre = [0]
for i in range(n):
    pre.append(pre[-1] + l[i])
calc(pre, t)
