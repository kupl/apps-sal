# Two cases:
# MaxSubarray = normal -> proceed normally
# MaxSubarray = circular -> total sum - minSubarray
# return max(maxSubarray, maxSubarraycircular
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total_sum = 0
        global_max = A[0]
        global_min = A[0]
        local_max = 0
        local_min = 0
        for num in A:
            local_max = max(num, local_max + num)
            local_min = min(num, local_min + num)
            global_max = max(global_max, local_max)
            global_min = min(global_min, local_min)
            total_sum += num

        circular_max = total_sum - global_min
        if global_max <= 0:
            return global_max
        return max(circular_max, global_max)
