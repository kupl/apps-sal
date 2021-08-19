class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        if n == 1:
            return A[0]
        global_max = float('-inf')
        global_min = float('inf')
        local_max = 0
        local_min = 0
        for (i, a) in enumerate(A):
            local_max = max(local_max + a, a)
            global_max = max(global_max, local_max)
            if 0 < i < n - 1:
                local_min = min(local_min + a, a)
                global_min = min(global_min, local_min)
        return max(global_max, sum(A) - global_min)
