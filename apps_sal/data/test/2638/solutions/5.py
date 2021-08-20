class Solution:

    def minimumTotal(self, triangle):
        mini = 100000000
        level = 0
        while level < len(triangle) - 1:
            for i in range(len(triangle[level + 1])):
                if i == 0:
                    triangle[level + 1][i] += triangle[level][i]
                elif i == len(triangle[level]):
                    triangle[level + 1][i] += triangle[level][i - 1]
                else:
                    triangle[level + 1][i] += min(triangle[level][i - 1], triangle[level][i])
            level += 1
        return min(triangle[len(triangle) - 1])
        '\n         :type triangle: List[List[int]]\n         :rtype: int\n         '
