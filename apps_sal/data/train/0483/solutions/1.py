class Solution:
     def maxArea(self, height):
         """
         :type height: List[int]
         :rtype: int
         """
         left_index = 0
         right_index = len(height) - 1
         water = 0
         while True:
             if left_index >= right_index:
                 break
             left_height = height[left_index]
             right_height = height[right_index]
             water = max(water, (right_index - left_index) * min(left_height, right_height))
             if left_height < right_height:
                 left_index += 1
             else:
                 right_index -= 1
         return water

