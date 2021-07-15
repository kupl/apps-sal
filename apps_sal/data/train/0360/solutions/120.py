from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = -1
        r = max(weights) * len(weights)
        
        def isOk(capacity):
            item = 0
            day = 0
            while item < len(weights):
                s = 0
                while True:
                    if weights[item] > capacity:
                        return False
                    if s + weights[item]> capacity:
                        break
                    else:
                        s = s + weights[item]
                        item += 1
                    if item >= len(weights):
                        break
                day += 1
            return day <= D


        while r - l > 1:
            mid = l + (r - l)//2
            if isOk(mid):
                r = mid
            else:
                l = mid
                
        return r


