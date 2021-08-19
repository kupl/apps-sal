class Solution:

    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False
        n = len(matrix[0])
        (lo, hi) = (0, len(matrix) * n)
        while lo < hi:
            mid = (lo + hi) / 2
            x = matrix[int(mid / n)][int(mid % n)]
            if x < target:
                lo = mid + 1
            elif x > target:
                hi = mid
            else:
                return True
        return False
        '\n         :type matrix: List[List[int]]\n         :type target: int\n         :rtype: bool\n         '
