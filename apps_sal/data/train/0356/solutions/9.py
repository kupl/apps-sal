class Solution:
    def searchMatrix(self, matrix, target):
        if (not matrix) or (target is None):
            return False
        rows, index = len(matrix[0]), len(matrix) * len(matrix[0])
        low, high = 0, index - 1
        while high >= low:
            mid = (low + high) // 2
            item = matrix[mid // rows][mid % rows]
            if item == target:
                return True
            elif item > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
