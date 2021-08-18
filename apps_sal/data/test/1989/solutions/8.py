import sys
from collections import Counter


class BIT():
    def __init__(self, n):
        self.n = n
        self.tree = [0] * n

    def _F(self, i):
        return i & (i + 1)

    def _getSum(self, r):
        '''
        sum on interval [0, r]
        '''
        result = 0
        while r >= 0:
            result += self.tree[r]
            r = self._F(r) - 1
        return result

    def getSum(self, l, r):
        '''
        sum on interval [l, r]
        '''
        return self._getSum(r) - self._getSum(l - 1)

    def _H(self, i):
        return i | (i + 1)

    def add(self, i, value=1):
        while i < self.n:
            self.tree[i] += value
            i = self._H(i)


reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__

n = int(input())
a = list(map(int, input().split()))


freq = BIT(n + 1)
f_left = [0] * n
f_right = [0] * n
ctr = Counter()
for i, val in enumerate(a):
    ctr[val] += 1
    f_left[i] = ctr[val]
for i in range(n):
    val = a[i]
    f_right[i] = ctr[val] - f_left[i] + 1
for f_r in f_right:
    freq.add(f_r, 1)
ans = 0
for i, f_l in enumerate(f_left):
    f_r = f_right[i]
    freq.add(f_r, -1)
    ans += freq.getSum(1, f_l - 1)
print(ans)
