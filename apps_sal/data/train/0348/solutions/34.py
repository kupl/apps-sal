class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        curr_max = [-math.inf, -math.inf]
        max_sum = -math.inf
        for num in arr:
            curr_max[0], curr_max[1] = max(num, curr_max[0] + num), max(curr_max[1] + num, curr_max[0])
            max_sum = max([max_sum, curr_max[0], curr_max[1]])
        
        return max_sum
