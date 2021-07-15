class Solution:
     def findMinMoves(self, machines):
         """
         :type machines: List[int]
         :rtype: int
         """
         sum_before = [0]
         i = 0
         for m in machines:
             sum_before.append(m + sum_before[i])
             i+=1
             
         if sum_before[len(machines)]%len(machines)!=0:
             return -1
         
         average = int(sum_before[len(machines)]/len(machines))
         
         result = 0
         
         i = 0
         for m in machines:
             left_require = average * i - sum_before[i] 
             right_require = average * (len(machines)-i-1) - (sum_before[len(machines)] - sum_before[i+1])
             if left_require > 0 and right_require > 0:
                 max_tran = left_require + right_require
             else:
                 max_tran = max(abs(left_require), abs(right_require))
             result = max(result, max_tran)
             i+=1
                 
         return result
