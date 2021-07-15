# method 1  append array's copy at back of it. then apply kadane's algorithm
# *not work* because we can only attain maximum n size window but here it can be 2n

# method 2  sliding window  max window size = n
# *not work* because there is no way to move back of window

# method 3  modified kadane's algorithm(see in lee215's solution)
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if not A:
            return 0
        
        max_sum, cur_max, min_sum, cur_min, total = A[0], 0, A[0], 0, 0
        for a in A:
            cur_max = max(a + cur_max, a)
            max_sum = max(max_sum, cur_max)
            
            cur_min = min(a + cur_min, a)
            min_sum = min(min_sum, cur_min)
            
            total += a
        
        return max(max_sum, total - min_sum) if total > min_sum else max_sum
