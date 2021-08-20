class Solution:

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == []:
            return 0
        l = len(height)
        p1 = 0
        p2 = l - 1
        area = 0
        while p1 < p2:
            if height[p1] <= height[p2]:
                area = max(area, height[p1] * (p2 - p1))
                p1 += 1
            else:
                area = max(area, height[p2] * (p2 - p1))
                p2 -= 1
        return area
