class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        def step(n, i) -> int:
            s = 0
            while n != 1:
                if n % 2 == 0:
                    n = n / 2
                else:
                    n = n * 3 + 1
                s += 1
            return s

        a = 0
        l = []
        for i in range(lo, hi + 1):
            a = step(i, 0)
            l.append((i, a))

        l = sorted(l, key=lambda x: x[1])
        return l[k - 1][0]
