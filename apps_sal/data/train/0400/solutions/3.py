class Solution:
     def largestRectangleArea(self, heights):
         """
         :type heights: List[int]
         :rtype: int
         """
         stk = []
         res = 0
         for i in range(len(heights)):
             if len(stk) == 0 or heights[i] >= heights[stk[-1]]:
                 stk.append(i)
             else:
                 end_p = stk[-1]
                 while len(stk) > 0 and heights[stk[-1]] >= heights[i]:
                     start_p = stk.pop()
                     res = max(res, (end_p - start_p + 1) * heights[start_p])
                 res = max(res, heights[i] * (i - start_p + 1))
                 heights[start_p] = heights[i]
                 stk.append(start_p)
                 stk.append(i)
             #print(res, stk)
         
         if len(stk) > 0:
             end_p = stk[-1]
             while len(stk) > 0:
                 start_p = stk.pop()
                 res = max(res, (end_p - start_p + 1) * heights[start_p])
                 #print(res)
         
         
         return res
                 
                 
                     
             
         

