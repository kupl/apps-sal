#!/usr/bin/env python3
import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, a):
        # Operator
        self.op = lambda a, b : a + b
        # Identity element
        self.e = 0 

        self.n = len(a)
        self.lv = (self.n - 1).bit_length()
        self.size = 2**self.lv
        self.data = [self.e] * (2*self.size - 1)
        # Bisect checking function 
        self._check = lambda x, acc : acc >= x
        self._acc = self.e

        self.initialize(a)

    # Initialize data
    def initialize(self, a):
        for i in range(self.n):
            self.data[self.size + i - 1] = a[i]
        for i in range(self.size-2, -1, -1):
            self.data[i] = self.op(self.data[i*2 + 1], self.data[i*2 + 2])

    # Update ak as x (0-indexed)
    def update(self, k, x):
        k += self.size - 1
        self.data[k] = x
        while k > 0:
            k = (k - 1) // 2
            self.data[k] = self.op(self.data[2*k+1], self.data[2*k+2])

    # Min value in [l, r) (0-indexed)
    def fold(self, l, r):
        L = l + self.size; R = r + self.size
        s = self.e
        while L < R:
            if R & 1:
                R -= 1
                s = self.op(s, self.data[R-1])
            if L & 1:
                s = self.op(s, self.data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

    def _bisect_forward(self, x, start, k):
        # When segment-k is at the bottom, accumulate and return.
        if k >= self.size - 1:
            self._acc = self.op(self._acc, self.data[k])
            if self._check(x, self._acc):
                return k - (self.size - 1)
            else:
                return -1
        width = 2**(self.lv - (k+1).bit_length() + 1)
        mid = (k+1) * width + width // 2 - self.size 
        # When left-child isn't in range, just look at right-child. 
        if mid <= start:
            return self._bisect_forward(x, start, 2*k + 2)
        # When segment-k is in range and has no answer in it, accumulate and return -1
        tmp_acc = self.op(self._acc, self.data[k])
        if start <= mid - width // 2 and not self._check(x, tmp_acc):
            self._acc = tmp_acc
            return -1
        # Check left-child then right-child
        vl = self._bisect_forward(x, start, 2*k + 1)
        if vl != -1:
            return vl
        return self._bisect_forward(x, start, 2*k + 2)
    
    # Returns min index s.t. start <= index and satisfy check(data[start:idx)) = True
    def bisect_forward(self, x, start=None):
        if start:
            ret = self._bisect_forward(x, start, 0)
        else:
            ret = self._bisect_forward(x, 0, 0)
        self._acc = self.e
        return ret

    def _bisect_backward(self, x, start, k):
        # When segment-k is at the bottom, accumulate and return.
        if k >= self.size - 1:
            self._acc = self.op(self._acc, self.data[k])
            if self._check(x, self._acc):
                return k - (self.size - 1)
            else:
                return -1
        width = 2**(self.lv - (k+1).bit_length() + 1)
        mid = (k+1) * width + width // 2 - self.size 
        # When right-child isn't in range, just look at right-child. 
        if mid >= start:
            return self._bisect_backward(x, start, 2*k + 1)
        # When segment-k is in range and has no answer in it, accumulate and return -1
        tmp_acc = self.op(self._acc, self.data[k])
        if start > mid + width // 2 and not self._check(x, tmp_acc):
            self._acc = tmp_acc
            return -1
        # Check right-child then left-child
        vl = self._bisect_backward(x, start, 2*k + 2)
        if vl != -1:
            return vl
        return self._bisect_backward(x, start, 2*k + 1)
    
    # Returns max index s.t. index < start and satisfy check(data[idx:start)) = True
    def bisect_backward(self, x, start=None):
        if start:
            ret = self._bisect_backward(x, start, 0)
        else:
            ret = self._bisect_backward(x, self.n, 0)
        self._acc = self.e
        return ret

n = int(input())
query = []
seen = set([0])
for _ in range(n):
    kind, val = map(int, input().split())
    query.append((kind, val))
    if val > 0: 
        seen.add(val)

unique = list(seen)
unique.sort()
comp = {val: i for i, val in enumerate(unique)}
decomp = {i: val for i, val in enumerate(unique)}
decopm = {}
nn = len(comp)

base = [0] * nn
STfire = SegmentTree(base)
STnum = SegmentTree(base)
STval = SegmentTree(base)

tnum = 0
fnum = 0
spell = 0
total = 0
for kind, val in query:
    cd = comp[abs(val)]
    if val > 0:
        STval.update(cd, val)
        STnum.update(cd, 1)
        total += val
        if kind == 1:
            tnum += 1
        else:
            STfire.update(cd, 1)
            fnum += 1
    else:
        total += val
        STval.update(cd, 0)
        STnum.update(cd, 0)
        if kind == 1:
            tnum -= 1
        else:
            STfire.update(cd, 0)
            fnum -= 1
    spell = tnum + fnum
    if fnum == 0:
        fid = -1
    else:
        fid = STfire.bisect_forward(fnum)
    l = STnum.bisect_forward(spell - tnum)
    if tnum == 0:
        print(total)
        continue
    if fid >= l + 1:
        double_total = STval.fold(l + 1, nn)
        print(total + double_total)
    else:
        l = STnum.bisect_forward(spell - tnum + 1)
        double_total = STval.fold(l + 1, nn)
        if fnum > 0:
            print(total + double_total + decomp[fid])
        else:
            print(total + double_total)
