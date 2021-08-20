class Solution:

    def __init__(self):
        self.d = {}

    def solve(self, x):
        if x == 1:
            return 0
        if self.d.get(x, 0) != 0:
            return self.d[x]
        if x % 2 == 0:
            self.d[x] = 1 + self.solve(x // 2)
            return self.d[x]
        else:
            self.d[x] = 1 + self.solve(x * 3 + 1)
            return self.d[x]

    def getKth(self, lo, hi, k):
        ar = []
        for i in range(hi, lo - 1, -1):
            ar.append((self.solve(i), i))
        ar.sort()
        return ar[k - 1][1]
