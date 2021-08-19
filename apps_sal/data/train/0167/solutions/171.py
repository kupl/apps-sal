from math import floor, log2


class Solution:

    def superEggDrop(self, k: int, n: int) -> int:
        best_case = floor(log2(n) + 1)
        if k >= best_case:
            return best_case

        def fast_sum(k, l):
            s = 0
            c = 1
            for i in range(k):
                c *= (l - i) / (i + 1)
                s += c
            return s
        if k == 0:
            return n
        (a, b) = (1, n)
        while a < b:
            c = (a + b) // 2
            if fast_sum(k, c) < n:
                a = c + 1
            else:
                b = c
        return a
