class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = 0

        if(len(matrix) == 0 or len(matrix[0]) == 0):
            return False
        while(i < len(matrix)):
            if(matrix[i][0] > target):
                break
            i += 1
        i -= 1

        target_vector = matrix[i]
        l = 0
        r = len(target_vector) - 1
        while(l <= r):
            mid = (l + r) // 2
            print((target_vector[mid]))
            if(target_vector[mid] == target):
                return True
            if(target_vector[mid] < target):
                l = mid + 1
            else:
                r = mid - 1
        return False
