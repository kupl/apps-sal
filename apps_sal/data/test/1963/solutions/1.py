import math


class SegmentTree:
    def __init__(self, data, default=0, func=lambda a, b: math.gcd(a, b)):
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


class SegmentTree1:
    def __init__(self, data, default=9999999999999999999999999999999, func=lambda a, b: min(a, b)):
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


n = int(input())
l = list(map(int, input().split()))
s2 = SegmentTree(l)
s1 = SegmentTree1(l)
s = 0
e = 0
d = dict()
d1 = dict()
ed = [] + l[::-1]
s3 = SegmentTree(ed)
s4 = SegmentTree1(ed)
d2 = dict()
while(s < n):
    if s in d1:
        d1[s] = e - s - 1
    else:
        d1.update({s: e - s - 1})
    if e == n:
        e -= 1
        s += 1
    if s2.query(s, e) == s1.query(s, e):
        e += 1
    else:
        s += 1
    if s > e:
        e += 1
    if e > n - 1:
        e = n
if s in d1:
    d1[s] = e - s - 1
else:
    d1.update({s: e - s - 1})
e = 0
s = 0
while(s < n):
    if s in d2:
        d2[n - 1 - s] = e - s - 1
    else:
        d2.update({n - 1 - s: e - s - 1})
    if e == n:
        e -= 1
        s += 1
    if s3.query(s, e) == s4.query(s, e):
        e += 1
    else:
        s += 1
    if s > e:
        e += 1
    if e > n - 1:
        e = n
if s in d2:
    d2[n - 1 - s] = e - s - 1
else:
    d2.update({n - 1 - s: e - s - 1})
ans = 0
# print(d1,d2)
for j in d1:
    if j in d2:
        if 0 <= j + d1[j] < n and 0 <= j - d2[j] < n and 0 <= j < n and s2.query(j, j + d1[j]) == s2.query(j - d2[j], j):
            d1[j] += d2[j]
    ans = max(ans, d1[j])
for j in d2:
    ans = max(ans, d2[j])
s = 0
e = s + ans
w = []
while(e < n):
    if s2.query(s, e) == s1.query(s, e):
        w.append(s + 1)
    s += 1
    e += 1
print(len(w), ans)
print(*w, sep=' ')
