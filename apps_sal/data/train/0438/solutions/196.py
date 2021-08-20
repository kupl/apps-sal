class Solution:

    def findLatestStep(self, A: List[int], m: int) -> int:
        (L, R, C, res) = ({}, {}, 0, -1)
        for (i, x) in enumerate(A):
            l = r = x
            if x - 1 in L:
                l = L[x - 1]
                if x - l == m:
                    C -= 1
                del L[x - 1]
            if x + 1 in R:
                r = R[x + 1]
                if r - x == m:
                    C -= 1
                del R[x + 1]
            (R[l], L[r]) = (r, l)
            if r - l + 1 == m:
                C += 1
            if C:
                res = i + 1
        return res
