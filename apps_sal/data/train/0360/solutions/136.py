class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right-left) // 2
            if self.__countDays(weights, mid) <= D:
                right = mid
            else:
                left = mid+1
        return left
        
    def __countDays(self, weights, capacity):
        days = 0
        cur_w = 0
        for w in weights:
            cur_w += w
            if cur_w > capacity:
                days += 1
                cur_w = w
        return days + 1
