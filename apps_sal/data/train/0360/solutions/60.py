#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def timeConsumption(limit):
            days = totalWeight = 0
            for weight in weights:
                if totalWeight + weight > limit:
                    days += 1
                    totalWeight = weight
                else:
                    totalWeight += weight
            return days + 1
        left = max(weights)
        right = sum(weights) + 1
        while left < right:
            mid = left + (right - left) // 2
            time = timeConsumption(mid)
            if time > D:
                left = mid + 1
            else:
                right = mid
        return left
