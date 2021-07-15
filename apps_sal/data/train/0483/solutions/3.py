class Solution:
     def maxArea(self, height):
         left, right = 0, len(height) - 1
         area = 0
         
         while left < right:
             if height[left] <= height[right]:
                 h = height[left]
                 tmp = (right - left) * h
                 left += 1
             else:
                 h = height[right]
                 tmp = (right - left) * h
                 right -= 1
             if area < tmp:
                 area = tmp
             
         return area
         """
         :type height: List[int]
         :rtype: int
         """

