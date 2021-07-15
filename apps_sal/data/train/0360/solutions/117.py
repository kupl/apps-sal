class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        low, high = max(weights), sum(weights)
            
        while low<high:
            mid = low + (high-low)//2
            d = 1
            curr_sum = 0
            for idx in range(len(weights)):
                if curr_sum + weights[idx] >mid:
                    d += 1
                    curr_sum =0
                curr_sum += weights[idx]
            
            if d <=D:
                high = mid
            else:
                low = mid+1
        return low
            

