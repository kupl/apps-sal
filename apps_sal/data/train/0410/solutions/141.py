from functools import cmp_to_key


class Solution:
    def getPower(self, number):
        if number == 1:
            return 0
        if number % 2 == 0:
            return 1 + self.getPower(number / 2)
        else:
            return 1 + self.getPower(number * 3 + 1)

    def getKth(self, lo: int, hi: int, k: int) -> int:
        a = []
        for i in range(lo, hi + 1):
            a.append((i, self.getPower(i)))
        a = sorted(a, key=cmp_to_key(
            lambda x, y: x[1] - y[1] if x[1] != y[1] else x[0] - y[0]))
        print(a)
        return a[k - 1][0]
