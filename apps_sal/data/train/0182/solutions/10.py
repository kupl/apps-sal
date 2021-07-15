class Solution:
     def trap(self, height):
         """
         :type height: List[int]
         :rtype: int
         """
         
         length = len(height)
         if(length == 0):
             return 0
         maxLeft = [0] * length
         maxRight = [0] * length
         result = 0
         maxLeft[0] = height[0]
         maxRight[length - 1] = height[length - 1]
         for i in range(1,length):
             maxLeft[i] = max(maxLeft[i - 1], height[i])
         for i in reversed(list(range(0, length - 1))):
             maxRight[i] = max(maxRight[i + 1], height[i])
         for i in range(length):
             result += min(maxLeft[i], maxRight[i]) - height[i]
         return result
 
                     
             
             

