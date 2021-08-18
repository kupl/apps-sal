import sys
input = sys.stdin.readline


class SegmentTree:
    def __init__(self, a):
        self.op = lambda a, b: max(a, b)
        self.e = 0

        self.n = len(a)
        self.lv = (self.n - 1).bit_length()
        self.size = 2**self.lv
        self.data = [self.e] * (2 * self.size - 1)
        self._check = lambda x, acc: acc >= x
        self._acc = self.e

        self.initialize(a)

    def initialize(self, a):
        for i in range(self.n):
            self.data[self.size + i - 1] = a[i]
        for i in range(self.size - 2, -1, -1):
            self.data[i] = self.op(self.data[i * 2 + 1], self.data[i * 2 + 2])

    def update(self, k, x):
        k += self.size - 1
        self.data[k] = x
        while k > 0:
            k = (k - 1) // 2
            self.data[k] = self.op(self.data[2 * k + 1], self.data[2 * k + 2])

    def fold(self, l, r):
        L = l + self.size
        R = r + self.size
        s = self.e
        while L < R:
            if R & 1:
                R -= 1
                s = self.op(s, self.data[R - 1])
            if L & 1:
                s = self.op(s, self.data[L - 1])
                L += 1
            L >>= 1
            R >>= 1
        return s

    def _bisect_forward(self, x, start, k):
        if k >= self.size - 1:
            self._acc = self.op(self._acc, self.data[k])
            if self._check(x, self._acc):
                return k - (self.size - 1)
            else:
                return -1
        width = 2**(self.lv - (k + 1).bit_length() + 1)
        mid = (k + 1) * width + width // 2 - self.size
        if mid <= start:
            return self._bisect_forward(x, start, 2 * k + 2)
        tmp_acc = self.op(self._acc, self.data[k])
        if start <= mid - width // 2 and not self._check(x, tmp_acc):
            self._acc = tmp_acc
            return -1
        vl = self._bisect_forward(x, start, 2 * k + 1)
        if vl != -1:
            return vl
        return self._bisect_forward(x, start, 2 * k + 2)

    def bisect_forward(self, x, start=None):
        if start:
            ret = self._bisect_forward(x, start, 0)
        else:
            ret = self._bisect_forward(x, 0, 0)
        self._acc = self.e
        return ret

    def _bisect_backward(self, x, start, k):
        if k >= self.size - 1:
            self._acc = self.op(self._acc, self.data[k])
            if self._check(x, self._acc):
                return k - (self.size - 1)
            else:
                return -1
        width = 2**(self.lv - (k + 1).bit_length() + 1)
        mid = (k + 1) * width + width // 2 - self.size
        if mid >= start:
            return self._bisect_backward(x, start, 2 * k + 1)
        tmp_acc = self.op(self._acc, self.data[k])
        if start > mid + width // 2 and not self._check(x, tmp_acc):
            self._acc = tmp_acc
            return -1
        vl = self._bisect_backward(x, start, 2 * k + 2)
        if vl != -1:
            return vl
        return self._bisect_backward(x, start, 2 * k + 1)

    def bisect_backward(self, x, start=None):
        if start:
            ret = self._bisect_backward(x, start, 0)
        else:
            ret = self._bisect_backward(x, self.n, 0)
        self._acc = self.e
        return ret


n = int(input())
s = input().rstrip()
array = [0] * n
ST = SegmentTree(array)

event = []
for i, ch in enumerate(s):
    event.append((ch, i))
event.sort(reverse=True)

ans = [0] * n
for ch, index in event:
    val = ST.fold(0, index) + 1
    ans[index] = val
    ST.update(index, val)
print(max(ans))
print(*ans)
