class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        global_max_sub = 1
        local_max = 1
        pre_diff = 0

        for i in range(1, len(A)):
            cur_diff = A[i] - A[i - 1]

            mul = cur_diff * pre_diff

            if cur_diff == 0:
                local_max = 1
            elif mul < 0:
                local_max += 1
            else:
                local_max = 2

            if local_max > global_max_sub:
                global_max_sub = local_max

            pre_diff = cur_diff

        return global_max_sub
