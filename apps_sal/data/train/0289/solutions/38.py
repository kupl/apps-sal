class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if not A:
            return 0
        ldp = [0 for i in range(len(A))]
        mdp = [0 for j in range(len(A))]
        sum_l = sum(A[len(A) - L:])
        for i in range(len(A) - L, -1, -1):
            sum_l = max(sum_l, sum(A[i:i + L]))
            ldp[i] = sum_l
        sum_m = sum(A[len(A) - M:])
        for i in range(len(A) - M, -1, -1):
            sum_m = max(sum_m, sum(A[i:i + M]))
            mdp[i] = sum_m
        print(ldp)
        print(mdp)
        ret = float('-inf')
        for i in range(len(A) - L - M + 1):
            ret = max(ret, sum(A[i:i + L]) + mdp[i + L], sum(A[i:i + M]) + ldp[i + M])
        return ret
