class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) == 1:
            return 1
        state = 1 if A[0] < A[1] else 0
        cnt = 1 if A[0] != A[1] else 0
        max_cnt = cnt
        for i in range(1, len(A) - 1):
            if (state == 1 and A[i] > A[i + 1]) or (state == 0 and A[i] < A[i + 1]):
                cnt += 1
                state = 1 - state
            else:
                max_cnt = max(max_cnt, cnt + 1)
                cnt = 1 if A[i] != A[i + 1] else 0
        max_cnt = max(max_cnt, cnt + 1)
        return max_cnt if max_cnt != 0 else 1

