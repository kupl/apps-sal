class Solution:

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        maxVal = 0
        cases = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, -1)]
        for case in cases:
            (a, b, c) = case
            (minimum, maximum) = (float('inf'), float('-inf'))
            for i in range(0, len(arr1)):
                minimum = min(minimum, a * arr1[i] + b * arr2[i] + c * i)
                maximum = max(maximum, a * arr1[i] + b * arr2[i] + c * i)
            maxVal = max(maxVal, maximum - minimum)
        return maxVal
