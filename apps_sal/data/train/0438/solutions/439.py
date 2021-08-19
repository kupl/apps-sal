class Tree:

    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi
        self.mid = None
        self.left = self.right = None

    def size(self):
        return self.hi - self.lo + 1

    def split(self, val, m):
        if self.mid != None:
            if val < self.mid:
                if self.left.size() == 1:
                    self.left = None
                else:
                    return self.left.split(val, m)
            elif val > self.mid:
                if self.right.size() == 1:
                    self.right = None
                else:
                    return self.right.split(val, m)
            return False
        if val == self.lo:
            self.lo = val + 1
            if self.hi - self.lo + 1 == m:
                return True
        elif val == self.hi:
            self.hi = val - 1
            if self.hi - self.lo + 1 == m:
                return True
        else:
            self.mid = val
            check = False
            if val - 1 >= self.lo:
                if val - self.lo == m:
                    return True
                self.left = Tree(self.lo, val - 1)
            if val + 1 <= self.hi:
                if self.hi - val == m:
                    return True
                self.right = Tree(val + 1, self.hi)
        return False


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return len(arr)
        root = Tree(1, len(arr))
        step = len(arr) - 1
        for i in range(len(arr) - 1, -1, -1):
            if root.split(arr[i], m):
                return step
            step -= 1
        return -1
