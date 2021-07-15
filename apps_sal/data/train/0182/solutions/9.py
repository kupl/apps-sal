class Solution:
     def trap(self, height):
         """
         :type height: List[int]
         :rtype: int
         """
         leftmaxes = []
         rightmaxes = []
         
         maximum = 0
         for i in range(len(height)):
             maximum = max(maximum, height[i])
             leftmaxes.append(maximum)
             
             
         maximum = 0
         for i in range(len(height)):
             maximum = max(maximum, height[len(height) - i - 1])
             rightmaxes.append(maximum)
         
         water = 0
         
         print(leftmaxes)
         print(rightmaxes)
         
         for i in range(len(height)):
             trappable = min(leftmaxes[i], rightmaxes[-i-1])
             if(trappable > height[i]):
                 water += trappable - height[i]
         
         return water

