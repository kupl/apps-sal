class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        sum_l = []
        sum_m = []
        for i in range(len(A) - L + 1):
            sum_l.append(sum(A[i: i+L]))
        for i in range(len(A) - M + 1):
            sum_m.append(sum(A[i: i+M]))
        res = 0
        for i in range(len(A) - L + 1):
            for j in range(len(A) - M + 1):
                if i + L <= j or i >= j + M:
                    res = max(res, sum_l[i] + sum_m[j])
        return res
