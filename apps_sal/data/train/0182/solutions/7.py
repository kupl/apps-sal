class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            mh = min(height[left], height[right])
            if height[left] < height[right]:
                left = left + 1
                while height[left] <= mh and left < right:
                    result = result + mh - height[left]
                    left = left + 1
            else:
                right = right - 1
                while height[right] <= mh and left < right:
                    result = result + mh - height[right]
                    right = right - 1

        return result
