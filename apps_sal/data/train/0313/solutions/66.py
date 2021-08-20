class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def feasible(days):
            cur = 0
            bou = 0
            for b in bloomDay:
                if b <= days:
                    cur += 1
                    if cur == k:
                        bou += 1
                        if bou >= m:
                            return True
                        cur = 0
                else:
                    cur = 0
            return False
        if m * k > len(bloomDay):
            return -1
        if m * k == len(bloomDay):
            return max(bloomDay)
        (l, r) = (min(bloomDay), max(bloomDay))
        while l < r:
            mid = l + (r - l) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l
