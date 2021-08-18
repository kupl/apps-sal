class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if not bloomDay:
            return -1
        if k * m > len(bloomDay):
            return -1

        def check(cur):
            res = 0
            curk = 0
            for item in bloomDay:
                if item <= cur:
                    curk += 1
                    if curk == k:
                        res += 1
                        curk = 0
                else:
                    curk = 0
            if res < m:
                return False
            return True

        b = min(bloomDay)
        e = max(bloomDay)
        rt = 0
        while b < e:

            mid = b + (e - b) // 2
            if check(mid):
                e = mid
            else:
                b = mid + 1
        return b

        return rt
