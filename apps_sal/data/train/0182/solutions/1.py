class Solution:
     def trap(self, height):
         """
         :type height: List[int]
         :rtype: int
         """
         # if len(height) < 3 :
         #     return 0
         # maxTrap = 0
         # stack=[]
         # i = 0
         # while i < len(height):
         #     if not stack or height[i] <= height[stack[-1]]:
         #         stack.append(i)
         #         i += 1
         #     else :
         #         bot = stack.pop()
         #         trap = 0 if not stack else (min(height[i],height[stack[-1]]) - height[bot] ) * (i-stack[-1]-1)
         #         maxTrap += trap
         #     # print(stack)
         # return maxTrap
         if not height :
             return 0
         left , right = 0 , len(height)-1
         maxLeft,maxRight = height[left],height[right]
         maxTrap = 0
         while left <= right :
             if height[left] <= height[right]:
                 if height[left] > maxLeft :
                     maxLeft = height[left]
                 else :
                     maxTrap += (maxLeft - height[left])
                 left += 1
             else :
                 if height[right] > maxRight:
                     maxRight = height[right]
                 else :
                     maxTrap += (maxRight -height[right])
                 right -= 1
         return maxTrap
