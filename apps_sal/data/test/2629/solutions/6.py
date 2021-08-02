class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        left = 0
        top = 0
        right = n - 1
        bottom = n - 1

        res = [[0 for _ in range(n)] for _ in range(n)]

        num = 1

        while left < right and top < bottom:
            for i in range(left, right):
                res[top][i] = num
                num += 1
            for i in range(top, bottom):
                res[i][right] = num
                num += 1
            for i in range(right, left, -1):
                res[bottom][i] = num
                num += 1
            for i in range(bottom, top, -1):
                res[i][left] = num
                num += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        if left == right and top == bottom:
            res[left][top] = num

        return res
