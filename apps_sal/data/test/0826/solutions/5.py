class BisectBase:

    def __init__(self, n, asc):
        self._n = n
        self._lc = self.ge_item if asc else self.le_item
        self._rc = self.gt_item if asc else self.lt_item

    def lt_item(self, idx, item):
        raise NotImplementedError("lt_item should be implemented")

    def gt_item(self, idx, item):
        raise NotImplementedError("gt_item should be implemented")

    def le_item(self, idx, item):
        raise NotImplementedError("le_item should be implemented")

    def ge_item(self, idx, item):
        raise NotImplementedError("ge_item should be implemented")

    def bisect_left(self, item):
        return self._bisect_left(item, 0, self._n)

    def _bisect_left(self, item, left, right):
        """区間 [left, right) での探索
        """
        if right - left == 1:
            return left + 1
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
            return left + 1
        mid = left + (right - left) // 2
        if self._rc(mid, item):
            return self._bisect_right(item, left, mid)
        else:
            return self._bisect_right(item, mid, right)


class Bisect(BisectBase):

    def gt_item(self, idx, item):
        return idx * (idx + 1) > item


n = int(input())
b = Bisect(n + 1, True)
m = b.bisect_right(2 * (n+1)) - 1
print((n + 1 - m))

