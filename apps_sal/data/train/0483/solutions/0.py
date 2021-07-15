class Solution:
     def maxArea(self, height):
         """
         :type height: List[int]
         :rtype: int
         """
         # l = []
         # maxH = 0
         # for i in range(len(height)-1, -1, -1):
         #     if height[i] > maxH:
         #         maxH = height[i]
         #         l.append((i, maxH))
         # maxArea = 0
         # for i in range(len(height)):
         #     for jl in l:
         #         if i >= jl[0]:
         #             break
         #         area = (jl[0] - i) * min(height[i], jl[1])
         #         if area > maxArea:
         #             maxArea = area
         # return maxArea
         
         left = 0
         right = len(height) - 1
         if height[left] > height[right]:
             minH = height[right]
             minIndex = right
         else:
             minH = height[left]
             minIndex = left
         area = (right - left) * minH
         maxArea = area
         
         while left != right:
             if minIndex == left:
                 while left != right:
                     left += 1
                     if height[left] > minH:
                         if height[left] > height[right]:
                             minH = height[right]
                             minIndex = right
                         else:
                             minH = height[left]
                             minIndex = left
                         break
                 area = (right - left) * minH
             else:
                 while left != right:
                     right -= 1
                     if height[right] > minH:
                         if height[right] > height[left]:
                             minH = height[left]
                             minIndex = left
                         else:
                             minH = height[right]
                             minIndex = right
                         break
                 area = (right - left) * minH
             if area > maxArea:
                 maxArea = area
         return maxArea
