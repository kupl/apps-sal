class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        maxTrap = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    maxTrap += (maxLeft - height[left])
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    maxTrap += (maxRight - height[right])
                right -= 1
        return maxTrap
