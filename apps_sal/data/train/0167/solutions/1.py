class Solution:

    def superEggDrop(self, K: int, N: int) -> int:

        def aux(t, k):
            ret = 0
            r = 1
            for i in range(1, K + 1):
                r *= t - i + 1
                r //= i
                ret += r
                if ret >= N:
                    break
            return ret
        (l, r) = (1, N)
        while l < r:
            m = (l + r) // 2
            if aux(m, K) < N:
                l = m + 1
            else:
                r = m
        return l
