class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = list()
        helper_stack = list()

        max_area = 0
        for i in heights:
            if not stack:
                stack.append(i)
            else:
                if i >= stack[-1]:
                    stack.append(i)
                else:
                    width = 0
                    helper_stack.append(i)
                    while(stack and stack[-1] > i):
                        width += 1
                        height = stack.pop()
                        helper_stack.append(i)
                        max_area = max(max_area, height * width)
                    while helper_stack:
                        stack.append(helper_stack.pop())
        width = 0
        while stack:
            width += 1
            height = stack.pop()
            max_area = max(max_area, height * width)

        return max_area
