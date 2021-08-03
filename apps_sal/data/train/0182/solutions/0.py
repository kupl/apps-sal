class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        result = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] <= height[right]:
                tmp = height[left]
                left += 1
                while left < right and height[left] <= tmp:
                    result += tmp - height[left]
                    left += 1
            else:
                tmp = height[right]
                right -= 1
                while left < right and height[right] <= tmp:
                    result += tmp - height[right]
                    right -= 1
        return result
