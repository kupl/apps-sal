class Solution:

    def superEggDrop(self, K: int, N: int) -> int:

        def f(t):
            a = 0
            r = 1
            for i in range(1, K + 1):
                r *= t - i + 1
                r //= i
                a += r
                if a >= N:
                    break
            return a
        (l, h) = (1, N)
        while l < h:
            m = (l + h) // 2
            if f(m) < N:
                l = m + 1
            else:
                h = m
        return l
