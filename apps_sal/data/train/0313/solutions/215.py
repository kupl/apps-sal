class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        a = bloomDay
        if len(a) < m * k:
            return -1

        def ck(n, m, k):
            c = 0
            b = 0
            for x in a:
                if x <= n:
                    c += 1
                    if c == k:
                        b += 1
                        if b == m:
                            return bool(1)
                        c = 0
                else:
                    c = 0
            return bool(0)

        def bs(m, k):
            l, r = min(a), max(a)
            while l < r:
                mid = (l + r) // 2
                if ck(mid, m, k):
                    r = mid
                else:
                    l = mid + 1
            return l
        return bs(m, k)
