class Solution:

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        ans = 0
        heights += [-1]
        for i in range(len(heights)):
            left = i
            while 1:
                if len(stack) == 0:
                    stack.append((heights[i], left))
                    break
                if stack[-1][0] < heights[i]:
                    stack.append((heights[i], left))
                    break
                elif stack[-1][0] == heights[i]:
                    break
                else:
                    ans = (i - stack[-1][1]) * stack[-1][0] if (i - stack[-1][1]) * stack[-1][0] > ans else ans
                    left = stack[-1][1]
                    del stack[-1]
        return ans
