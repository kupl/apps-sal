class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        lst = []

        def power(s) -> int:
            count = 0
            while s != 1:
                if s % 2 == 0:
                    s = s // 2
                    count = count + 1
                else:
                    s = 3 * s + 1
                    count = count + 1
            return (count, s)
        for i in range(lo, hi + 1):
            lst.append((i, power(i)))
        lst.sort(key=lambda x: x[1])
        return lst[k - 1][0]
