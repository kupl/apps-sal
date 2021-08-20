class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def isValid(val):
            count = 0
            tmp = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= val:
                    tmp += 1
                    if tmp == k:
                        count += 1
                        if count == m:
                            return True
                        tmp = 0
                else:
                    tmp = 0
            return False
        ls = len(bloomDay)
        if m * k > ls:
            return -1
        (l, r) = (min(bloomDay), max(bloomDay))
        while l < r:
            mid = (l + r) // 2
            if isValid(mid):
                r = mid
            else:
                l = mid + 1
        return l
