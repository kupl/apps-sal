class Solution:
    def canShip(self, weights, capacity, D) -> bool:
        cnt, i = 0, 0
        cum = 0
        while i < len(weights):
            if cum + weights[i] <= capacity:
                cum += weights[i]
                i += 1
            else:
                cnt += 1
                cum = 0
        cnt += 1
        return cnt <= D
        
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            if self.canShip(weights, mid, D):
                r = mid
            else:
                l = mid + 1
        return r
