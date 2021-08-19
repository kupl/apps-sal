class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        (l, r) = (max(weights), sum(weights))
        while l < r:
            mid = (l + r) // 2
            cnt = 1
            cursum = 0
            for weight in weights:
                if cursum + weight <= mid:
                    cursum += weight
                else:
                    cnt += 1
                    cursum = weight
            if cnt <= D:
                r = mid
            else:
                l = mid + 1
        return r
