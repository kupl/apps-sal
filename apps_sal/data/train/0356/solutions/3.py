class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        print((len(matrix)))
        if(len(matrix) == 0):
            return False
        if len(matrix) == 1 and len(matrix[0]) == 0:
            return False
        existFlag = 0
        last = len(matrix[0]) - 1
        for i in range(len(matrix)):
            if matrix[i][last] < target:
                continue
            else:
                print("falg set to 1")
                existFlag = 1
                break
        if existFlag == 1:
            print("yes it is 1")
            for j in range(last, -1, -1):
                print(("j= ", j))
                if matrix[i][j] == target:
                    return True
        return False
