class Solution:
    def canBeFerried(self, weights: List[int], D: int, capacity: int) -> bool:
        i, j, days = 0, 0, 0
        while i < len(weights):
            sum_ = 0
            j = 0
            while (sum_ <= capacity):
                if (i + j < len(weights)):
                    sum_ += weights[i + j]
                else:
                    days += 1
                    return days <= D
                j += 1
            # print(f\"After exiting second loop: sum_ = {sum_}, j = {j}\")
            days += 1
            # print(f\"Increased days to {days}\")
            
            if i == len(weights) - 1:
                break
            i += j - 1
            # print(f\"Set i = {i}\")
            if days > D:
                return False
        return days <= D
            
    
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        low = max(weights)
        high = len(weights) * low
        
        while low < high:
            mid = (low + high) // 2
            if self.canBeFerried(weights, D, mid):
                high = mid
            else:
                low = mid + 1
        return low

