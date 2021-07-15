class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        currMaxSum = 0
        currMinSum = 0
        maxSum = float('-inf')
        minSum = float('inf')
        flag = False
        
        totalSum = 0
        
        for i in range(len(A)):
            currMaxSum += A[i]
            maxSum = max(maxSum, currMaxSum)
            if currMaxSum < 0:
                currMaxSum = 0

            
            totalSum += A[i]
            if A[i] >= 0: 
                flag = True
            
            currMinSum += A[i]
            minSum = min(minSum, currMinSum)
            if currMinSum > 0:
                currMinSum = 0
            
        if flag:
            return max(totalSum-minSum, maxSum)
        else:
            return maxSum
                
 
            
        
            

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#             currMaxSum = 0
#             currMinSum = 0
#             flag = False
#             maxSum = float('-inf')
#             minSum = float('inf')
#             totalSum = 0
            
#             for i in range(len(A)):
                
#                 currMaxSum += A[i]
#                 maxSum = max(maxSum, currMaxSum)
#                 if currMaxSum < 0:
#                     currMaxSum = 0
                    
#                 totalSum += A[i]
#                 if A[i] >= 0:
#                     flag = True
                    
                 
#                 currMinSum += A[i]
#                 minSum = min(minSum, currMinSum)
#                 if currMinSum > 0:
#                     currMinSum = 0
                    
#             if not flag:
#                 return maxSum 

#             else:
#                 return max(maxSum, totalSum-minSum)
            
                    
                
                

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#         ans1 = cur = None 
#         for x in A:
#             cur = x + max(cur, 0)
#             ans1 = max(ans1, cur)
            
#         ans2 = cur = float(\"inf\")
#         for i in range(1, len(A)):
#             cur = A[i] + min(cur, 0)
#             ans2 = min(ans2, cur)
#         ans2 = sum(A) - ans2
        
#         ans3 = cur = float(\"inf\")
#         for i in range(len(A)-1):
#             cur = A[i] + min(cur, 0)
#             ans3 = min(ans3, cur)
#         ans3 = sum(A) - ans3
        
#         return max(ans1, ans2, ans3)
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         track = [[0 for j in range(len(A))] for j in range(len(A))]
#         max_val = min(A)
#         for i in range(len(A)):
#             track[i][i] = A[i]
#             for j in range(i+1, len(A)):
#                     track[i][j] = track[i][j-1] + A[j]
#                     max_val = max(max_val, track[i][j])
#             max_val = max(max_val, track[i][i])
                    
#         #print(track)
#         for i in range(len(A)-1, 0, -1):
#             for j in range(0, i):
#                 track[i][j] = track[i][len(track) - 1] + track[0][j]
#                 max_val = max(max_val, track[i][j])
                
#         #print(track)
#         return max_val]

