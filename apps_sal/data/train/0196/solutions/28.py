# case1: ---------|

# case2: ---------|----------
#             |--------|
#              suf  pre
#        maxsubarray = total - min(subarray)


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        local_min = 0
        local_max = 0
        global_min = A[0]
        global_max = A[0]
        total = 0
        for num in A:
            total += num
            local_min = min(local_min + num, num)
            global_min = min(global_min, local_min)
            local_max = max(local_max + num, num)
            global_max = max(global_max, local_max)

        if global_max < 0:
            return global_max
        else:
            return max(global_max, total - global_min)
