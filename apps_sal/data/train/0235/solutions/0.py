class Solution:
     def numberOfArithmeticSlices(self, A):
         curr, sum = 0, 0
         for i in range(2,len(A)):
             if A[i]-A[i-1] == A[i-1]-A[i-2]:
                 curr += 1
                 sum += curr
             else:
                 curr = 0
         return sum
 #         solution = 0
 #         connected = 1
 #         old_diff = None
 #         sequences = []
 #         if len(A) < 3:
 #             return 0
         
 #         for index,num in enumerate(A):
 #             if index < len(A) - 1:
 #                 new_diff = num - A[index + 1]
 #             else:
 #                 new_diff = A[index - 1] - num
 #             if old_diff == new_diff:
 #                 if index == len(A) - 1 and connected >= 3:
 #                     connected += 1
 #                     sequences.append(connected)
 #                 connected += 1
 #             else:
 #                 old_diff = new_diff
 #                 if connected > 2:
 #                     sequences.append(connected)
 #                 connected = 1
 #         for sequence in sequences:
 #             prev = 0
 #             while sequence >= 2:
 #                 prev += 1
 #                 solution += prev
 #                 sequence -= 1
 #         return solution

