class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k or k == 0:
            return -1
        if n == m * k:
            return max(bloomDay)

        def isGood(days):
            kk = 0
            mm = 0
            i = 0
            while i < len(bloomDay):
                if bloomDay[i] <= days:
                    while i < len(bloomDay) and bloomDay[i] <= days and kk < k:
                        i += 1
                        kk += 1
                    if kk == k:
                        mm += 1
                        kk = 0
                else:
                    kk = 0
                    i += 1
                if mm == m:
                    return True
            return False

        low, high = 0, max(bloomDay)
        while low < high:
            mid = low + (high - low) // 2
            if isGood(mid):
                high = mid
            else:
                low = mid + 1
        return low
