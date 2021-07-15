class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # minDay
        # we need k consecutive elems in bloomDay list where all those elems <= minDay
        # we need m such groups
        
        # minimum possible val is min val in the list
        # maxmimum possible val is max val in the list
        # impossible case: m * k > list size
        
        if m * k > len(bloomDay):
            return -1
        
        def condition(minDay):
            numB = m
            curF = 0
            for day in bloomDay:
                if day <= minDay:
                    curF += 1
                    if curF == k:
                        numB -= 1
                        curF = 0
                    if numB == 0:
                        break
                else:
                    curF = 0
            return numB == 0
        
        l = min(bloomDay)
        r = max(bloomDay)
        # possible = 0
        while l < r:
            mid = l + (r - l) // 2
            if condition(mid):
                r = mid
            else:
                l = mid + 1
       
        return l
