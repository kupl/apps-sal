class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        def expr(sign1, sign2, i):
            return sign1 * arr1[i] + sign2 * arr2[i] + i

        def diff(sign1, sign2):
            max_ = max(expr(sign1, sign2, i) for i in range(len(arr1)))
            min_ = min(expr(sign1, sign2, i) for i in range(len(arr1)))
            return max_ - min_

        return max(diff(sign1, sign2) for sign1, sign2 in [(1, 1), (1, -1), (-1, 1), (-1, -1)])
