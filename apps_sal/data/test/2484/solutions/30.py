from operator import *
from copy import *


class TP:

    def __init__(self, cond, init=0, right=add, left=sub):
        self.cond = cond
        self.init = init
        self.next_right = right
        self.next_left = left

    def __call__(self, A, uniq=True):
        cond = self.cond
        (next_right, next_left) = (self.next_right, self.next_left)
        s = deepcopy(self.init)
        n = len(A)
        X = {}
        r = 0
        for l in range(n):
            if not uniq:
                X[l] = r
            while r < n and cond(s, A[r]):
                s = next_right(s, A[r])
                r += 1
                X[l] = r
            if l == r:
                r += 1
            else:
                s = next_left(s, A[l]) if l + 1 != r else deepcopy(self.init)
        return list(X.items())

    def maximum(self, A):
        X = self.__call__(A)
        return max((r - l for (l, r) in X)) if X else 0

    def count(self, A):
        X = self.__call__(A, False)
        return sum((r - l for (l, r) in X))


(n, *a) = map(int, open(0).read().split())
print(TP(lambda s, n: s + n == s ^ n).count(a))
