class Solution:
     def maxArea(self, height):
         """
         :type height: List[int]
         :rtype: int
         
         idea:
         Shorter coordinate determines the water size
         """
         
         if len(height) < 2: return False
         if len(height) == 2: return min(height[0], height[1])
         
         current_highest = 0
         i, j = 0, len(height) - 1
         while i < j:
             left = height[i]
             right = height[j]
             current_highest = max(current_highest, min(left, right) * (j - i))
             if right > left:
                 i += 1
             else:
                 j -= 1
         return current_highest
