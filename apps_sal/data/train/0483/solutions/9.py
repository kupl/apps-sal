class Solution:

    # two pointer, O(N) time
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:

            # area = height * width
            area = min(height[left], height[right]) * (right - left)

            if area > max_area:

                max_area = area

            if height[left] < height[right]:

                left += 1

            else:

                right -= 1

        return max_area
