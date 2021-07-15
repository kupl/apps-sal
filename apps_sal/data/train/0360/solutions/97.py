class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = 0
        r = sum(weights)
        best = r
        while l <= r:
            mid = l + (r - l) // 2
            if self.works(mid, weights, D):
                best = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return best
    
    def works(self, cap, weights, d):
        if cap < max(weights):
            return False
        idx = 0
        total_days = 0
        while idx < len(weights):
            cur_cap = 0
            while cur_cap < cap and idx < len(weights):
                if cur_cap + weights[idx] > cap:
                    break
                cur_cap += weights[idx]
                idx += 1
            
            total_days += 1
        
        return total_days <= d

