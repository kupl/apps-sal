class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, r = max(weights), sum(weights)

        def checkCapacity(maxCap):
            day = 1
            temp = 0
            for i in weights:
                temp += i
                if temp > maxCap:
                    temp = i
                    day += 1
                if day > D:
                    return False
            return True

        while l < r:
            mid = l + (r - l) // 2
            if checkCapacity(mid):
                r = mid
            else:
                l = mid + 1

        return l
