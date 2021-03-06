class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = left * len(weights) // D

        def checkShipping(cap):
            days = 1
            onboard = 0
            for (i, v) in enumerate(weights):
                if onboard + v > cap:
                    days += 1
                    onboard = v
                else:
                    onboard += v
                if days > D:
                    return False
            return True
        while left < right:
            mid = left + (right - left) // 2
            if checkShipping(mid):
                right = mid
            else:
                left = mid + 1
        return left
