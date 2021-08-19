class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        if not heights:
            return 0
        stack = [0]
        heights.append(0)
        # print(heights)
        max_area = 0
        for i in range(len(heights)):
            # print(stack)
            if heights[i] >= stack[-1]:
                stack.append(heights[i])
            else:
                k = len(stack) - 1
                count = 0
                while heights[i] < stack[k] and k >= 0:
                    count += 1
                    # print(count)
                    # print(stack[k])
                    area = count * stack[k]
                    if max_area < area:
                        max_area = area
                    k -= 1
                    # print(max_area)
                stack = stack[:-count] + [heights[i], ] * (count + 1)
                # print((count + 1) * stack[k])
                # if max_area < (count + 1) * heights[i]:
                # max_area = (count + 1) * heights[i]
        return max_area
