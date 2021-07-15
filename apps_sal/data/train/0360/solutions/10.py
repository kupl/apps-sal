class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        #Lower bound has to be the maximum of the weight to ship all weights
        #Upper bound is the sum of the weights (can ship all packages in one day)

        left, right = max(weights), sum(weights)
        while left < right:
            mid, need, cur = int((left + right) / 2), 1, 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D: left = mid + 1
            else: right = mid
        return left
