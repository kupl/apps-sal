class Solution:

    def maxTurbulenceSize(self, A) -> int:
        if len(A) <= 1:
            return len(A)
        if len(set(A)) == 1:
            return 1
        else:
            B = []
            for (idx, num) in enumerate(A[1:], start=1):
                B.append(A[idx] - A[idx - 1])
            max_len = 2
            C = []
            for num in B:
                if num > 0:
                    C.append(1)
                elif num == 0:
                    C.append(0)
                else:
                    C.append(-1)
            len_diff = 1
            for (idx, num) in enumerate(C[1:], start=1):
                if C[idx] * C[idx - 1] < 0:
                    if len_diff == 1:
                        len_diff += 1
                    len_diff = len_diff + 1
                elif C[idx] * C[idx - 1] == 0:
                    len_diff = 1
                else:
                    len_diff = 1
                max_len = max(len_diff, max_len)
        return max_len
