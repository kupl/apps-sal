class Solution:

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        (ans, stack) = (0, [])
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1] if stack else i
                ans = max(ans, h * w)
            stack.append(i)
        while stack:
            h = heights[stack.pop()]
            w = len(heights) - 1 - stack[-1] if stack else len(heights)
            ans = max(ans, h * w)
        return ans
