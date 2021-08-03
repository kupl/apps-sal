class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        a = [i for i in range(lo, hi + 1)]
        z = []

        def cv(s, c):
            if s == 1:
                c = c + 1
                return c
            if s % 2 == 0:
                s = s / 2
            else:
                s = 3 * s + 1
            c = c + 1
            if s == 1:
                return c
            return cv(s, c)
        for i in a:
            c = 0
            b = cv(i, c)
            z.append([b, i])
        z.sort(key=lambda x: x[0])
        a = []
        for i in z:
            a.append(i[1])
        return a[k - 1]
