class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
    
    # search space
    # MIN (LEFT) has to be at least the largest weight of the packages, otherwise boat cannot carry it
    # MAX (RIGHT) is the sum of all packages, since boat can carry all of it in ONE day
        left = 0
        right = 0
        for i in range(len(weights)):
            left = max(weights[i], left)
            right += weights[i]

        while left < right:
            mid = (left+right)//2

            if self.greedy_match(mid, weights, D):
                right = mid
            else:
                left = mid + 1

        return left
    
    
    
    
    
    
    
    
    
    
    
    def greedy_match(self, boat_weight, weights, days):
        cur_days = 1
        cur_weight = 0
        for i in range(len(weights)):
            if cur_weight + weights[i] > boat_weight:
                cur_weight = 0
                cur_days += 1
                if cur_days > days:
                    return False
            cur_weight += weights[i]
        return True

