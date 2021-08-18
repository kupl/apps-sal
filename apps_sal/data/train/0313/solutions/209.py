class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def fesible(mid):
            c, n, l = 0, 0, []
            b = [(i - mid) for i in bloomDay]
            for i in range(len(b)):
                if b[i] <= 0 and i != (len(b) - 1):
                    c += 1
                elif b[i] <= 0 and i == (len(b) - 1):
                    c += 1
                    l.append(c)
                elif b[i] > 0:
                    l.append(c)
                    c = 0

            ss = 0
            for i in l:
                ss += i // k
            if ss >= m or m * k <= max(l):
                return True
            return False

        v = 0
        left, right = min(bloomDay), max(bloomDay) + 1
        while left < right:
            mid = left + (right - left) // 2
            if fesible(mid):
                right = mid
                v = 1
            else:
                left = mid + 1
        if v == 0:
            return -1
        return left
