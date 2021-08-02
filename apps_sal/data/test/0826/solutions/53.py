from abc import ABCMeta, abstractmethod


class BisectBase(metaclass=ABCMeta):

    def __init__(self, n, asc):
        self._n = n
        self._lc = self._ge if asc else self._le
        self._rc = self._gt if asc else self._lt

    @abstractmethod
    def get(self, idx):
        pass

    def _lt(self, idx, item):
        return self.get(idx) < item

    def _gt(self, idx, item):
        return self.get(idx) > item

    def _le(self, idx, item):
        return self.get(idx) <= item

    def _ge(self, idx, item):
        return self.get(idx) >= item

    def bisect_left(self, item):
        return self._bisect_left(item, 0, self._n)

    def _bisect_left(self, item, left, right):
        """区間 [left, right) での探索
        """
        if right - left == 1:
            return left if self._lc(left, item) else left + 1
        mid = left + (right - left) // 2
        if self._lc(mid, item):
            return self._bisect_left(item, left, mid)
        else:
            return self._bisect_left(item, mid, right)

    def bisect_right(self, item):
        return self._bisect_right(item, 0, self._n)

    def _bisect_right(self, item, left, right):
        """区間 [left, right) での探索
        """
        if right - left == 1:
            return left if self._rc(left, item) else left + 1
        mid = left + (right - left) // 2
        if self._rc(mid, item):
            return self._bisect_right(item, left, mid)
        else:
            return self._bisect_right(item, mid, right)


class Bisect(BisectBase):

    def get(self, idx):
        return idx * (idx + 1)


n = int(input())
b = Bisect(n + 2, True)
m = b.bisect_right(2 * (n + 1)) - 1
print((n + 1 - m))
