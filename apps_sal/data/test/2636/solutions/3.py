class Solution:
     def getSkyline(self, blds):
         """
         :type buildings: List[List[int]]
         :rtype: List[List[int]]
         """
         if not blds:
             return []
         if len(blds) == 1:
             return [[blds[0][0], blds[0][2]], [blds[0][1], 0]]
         
         mid = len(blds) >> 1
         left = self.getSkyline(blds[:mid])
         right = self.getSkyline(blds[mid:])
         return self.merge(left, right)
         #conquor how to merge left and right
     
     def merge(self, left, right):
         res = []
         h1 = h2 = 0
         while left and right:
             if left[0][0] < right[0][0]:
                 pos, h1 = left.pop(0)
             elif right[0][0] < left[0][0]:
                 pos, h2 = right.pop(0)
             else:
                 pos, h1 = left.pop(0)
                 h2 = right.pop(0)[1]
             h = max(h1, h2)
             if not res or res[-1][1] != h:
                 res.append([pos, h])
                 
 
         if left:
             res += left
         if right:
             res += right
         return res
