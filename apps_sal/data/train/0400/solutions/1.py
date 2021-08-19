class Solution:

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        max_area = 0
        stack = []
        i = 0
        while i < len(heights):
            while i < len(heights) and (len(stack) == 0 or heights[i] > heights[stack[-1]]):
                stack.append(i)
                i += 1
            tmp = stack.pop()
            if stack:
                area = heights[tmp] * (i - stack[-1] - 1)
            else:
                area = heights[tmp] * i
            max_area = max(area, max_area)
        while stack:
            tmp = stack.pop()
            if stack:
                area = heights[tmp] * (i - stack[-1] - 1)
            else:
                area = heights[tmp] * i
            max_area = max(area, max_area)
        return max_area
