from sys import maxsize


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        i = 1
        n = len(A)
        # A=A+A
        # end = n
        ans = A[0]
        ans_max = A[0]
        ans_min = A[0]
        ans_f = A[0]
        sumi = A[0]
        while i < n:
            sumi += A[i]
            if ans + A[i % n] > A[i % n]:
                ans += A[i % n]
            else:
                ans = A[i % n]

            if ans_f + A[i % n] < A[i % n]:
                ans_f += A[i % n]
            else:
                ans_f = A[i % n]
            ans_max = max(ans_max, ans)
            ans_min = min(ans_min, ans_f)
            i += 1

        return max(ans_max, sumi - ans_min) if ans_min != sumi else ans_max
