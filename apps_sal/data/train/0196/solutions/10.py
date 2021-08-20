class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:

        def kadane(array):
            global_max = array[0]
            local_max = array[0]
            for i in range(1, len(array)):
                if local_max < 0:
                    local_max = 0
                local_max = array[i] + local_max
                if local_max > global_max:
                    global_max = local_max
            return global_max

        def kadane_inverse(array):
            global_min = array[0]
            local_min = array[0]
            for i in range(1, len(array)):
                if local_min > 0:
                    local_min = 0
                local_min = array[i] + local_min
                if local_min < global_min:
                    global_min = local_min
            return global_min
        total = sum(A)
        inv = kadane_inverse(A)
        reg = kadane(A)
        if total == inv:
            return reg
        return max(total - inv, reg)
