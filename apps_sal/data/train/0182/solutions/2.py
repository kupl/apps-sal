class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxRight = 0
        maxLeft = 0
        left = 0
        right = len(height) - 1
        ret = 0
        while left < right:
            maxRight = max(maxRight, height[right])
            maxLeft = max(maxLeft, height[left])
            if maxLeft > maxRight:
                ret += maxRight - height[right]
                right -= 1
            else:
                ret += maxLeft - height[left]
                left += 1
        return ret
