def binarySearchCount(arr, n, key):
    left = 0
    right = n - 1
    count = 0
    while left <= right:
        mid = int((right + left) / 2)
        if arr[mid] < key:
            count = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return count


def countGreater(arr, n, k):
    l = 0
    r = n - 1
    leftGreater = n
    while l <= r:
        m = int(l + (r - l) / 2)
        if arr[m] > k:
            leftGreater = m
            r = m - 1
        else:
            l = m + 1
    return n - leftGreater


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
        return 'SegmentTree({0})'.format(self.data)


(m, n) = map(int, input().split())
b = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
b.sort()
tot = 9999999999999999999999999999999
s = SegmentTree(a)
s1 = SegmentTree(b)
for i in range(n):
    c = binarySearchCount(b, m, a[i])
    ans = c * a[i] - s1.query(0, c - 1) - (n - 1 - i) * a[i] + s.query(i + 1, n - 1)
    tot = min(ans, tot)
for i in range(m):
    c = countGreater(a, n, b[i])
    ans = -c * b[i] + s.query(n - c, n - 1) - s1.query(0, i - 1) + i * b[i]
    tot = min(ans, tot)
print(tot)
