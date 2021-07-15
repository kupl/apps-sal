import math

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        sum_ = sum(weights)
        max_weight = max(weights)
        if D == 1:
            return sum_
        
        def check_capacity_enough(weights, D, capac):
            temp_cargo = 0
            count_ships = 1
            for i in range(len(weights)):
                if temp_cargo + weights[i] <= capac:
                    temp_cargo += weights[i]
                else:
                    count_ships += 1
                    if count_ships > D:
                        return False
                    temp_cargo = weights[i]
            return True
        
        def binary_search(weights, D, sum_, max_weight):
            left = max(math.floor(sum_/D) - 1, max_weight-1) 
            right = max(math.ceil(2*sum_/D)+1, max_weight+3) 
            while right-left >= 2:
                mid = (left + right)//2
                if mid >= max_weight and check_capacity_enough(weights, D, mid):
                    right = mid
                else:
                    left = mid
            return right
        
        return binary_search(weights, D, sum_, max_weight)
