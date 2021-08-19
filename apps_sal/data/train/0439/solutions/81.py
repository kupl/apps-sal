class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) <= 1:
            return len(A)
        current_len = max_len = 0
        prev_less = prev_great = True
        for i in range(1, len(A)):
            if A[i - 1] > A[i] and prev_less:
                current_len += 1
                prev_less = False
                prev_great = True
            elif A[i - 1] < A[i] and prev_great:
                current_len += 1
                prev_less = True
                prev_great = False
            else:
                max_len = max(max_len, current_len + 1)
                if A[i - 1] > A[i]:
                    current_len = 1
                    prev_less = False
                    prev_great = True
                elif A[i - 1] < A[i]:
                    current_len = 1
                    prev_less = True
                    prev_great = False
                else:
                    current_len = 0
                    prev_less = prev_great = True
        return max(max_len, current_len + 1)
