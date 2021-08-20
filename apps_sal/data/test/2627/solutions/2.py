class Solution:

    def __init__(self):
        self.maxarea = 0

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        def maxrect(height):
            height.append(0)
            stack = [-1]
            ans = 0
            for i in range(len(height)):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)
            height.pop()
            return ans
        abs_max = 0
        height = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    height[j] = 0
                else:
                    height[j] += 1
            local_max = maxrect(height)
            if local_max > abs_max:
                abs_max = local_max
        return abs_max
