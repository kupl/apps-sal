class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) <= 1:
            return len(A)

        res = 1
        comparison_sign = 0
        longest_curr = 0
        for i in range(1, len(A)):
            num = A[i]
            prev_num = A[i - 1]
            curr_comaprion_sign = A[i] - A[i - 1]
            if comparison_sign == 0 and curr_comaprion_sign != 0:
                longest_curr = 2
                res = max(res, longest_curr)
            else:
                if (curr_comaprion_sign > 0 and comparison_sign < 0) or (curr_comaprion_sign < 0 and comparison_sign > 0):

                    longest_curr += 1
                    res = max(res, longest_curr)
                else:
                    longest_curr = 2

            comparison_sign = curr_comaprion_sign

        return res
