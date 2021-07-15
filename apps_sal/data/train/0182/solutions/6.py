class Solution:
     '''Complexity O(n)'''
 
     def trap(self, height):
         n = len(height)
         l, r, water, minHeight = 0, n - 1, 0, 0
 
         while l < r:
             while l < r and height[l] <= minHeight:
                 water += minHeight - height[l]
                 l += 1
 
             while r > l and height[r] <= minHeight:
                 water += minHeight - height[r]
                 r -= 1
 
             minHeight = min(height[l], height[r])
 
         return water
