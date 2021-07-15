class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
        
        diff_dict = {}
        max_ = 0
        for i in range(len(A)):
            diff_dict[i] = {}
            for j in range(i):
                diff = A[i] - A[j]
                if diff in diff_dict[j]:
                    diff_dict[i][diff] = diff_dict[j][diff] + 1
                else:
                    diff_dict[i][diff] = 1
                    
                max_ = max(max_, diff_dict[i][diff])
             
        return max_ + 1
                
                

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         diff_dict = {}
#         max_ = 0
#         for i in range(len(A)):
#             diff_dict[i] = {}
#             for j in range(i):
#                 diff = A[i] - A[j]
                
#                 if diff in diff_dict[j]:
#                     diff_dict[i][diff] = diff_dict[j][diff] + 1
                
#                 else:
#                     diff_dict[i][diff] = 1
                
                
#                 max_ = max(max_, diff_dict[i][diff])
                
#         return max_
                
                
                
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#         diff_dict = {}
#         max_ = 0
#         for i in range(len(A)):
#             diff_dict[i] = {}
#             for j in range(i):
#                 curr = A[i]
#                 prev = A[j]

#                 diff = curr - prev 
#                 if diff in diff_dict[j]:
#                     diff_dict[i][diff] = diff_dict[j][diff] + 1
#                 else:
#                     diff_dict[i][diff] = 1

#                 max_ = max(max_, diff_dict[i][diff])

#         return (max_ + 1)

                
            
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         diff_dict = {}
#         max_ = 0
#         for i in range(len(A)):
#             diff_dict[i] = {}
#             for j in range(i):
#                 curr = A[i]
#                 prev = A[j]
                
#                 diff = curr - prev
                
#                 if diff in diff_dict[j]:
#                     diff_dict[i][diff] =  diff_dict[j][diff] + 1
#                 else:
#                     diff_dict[i][diff] = 1
                    
#                 max_ = max(max_, diff_dict[i][diff])
#         print(diff_dict)
#         return (max_ + 1)
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         mapping = {}
#         if len(A) < 2:
#             return len(A)
#         max_ = 0
    
#         for i in range(len(A)):
#             mapping[i] = {}
#             for j in range(0, i):
#                 diff = A[i] - A[j]
                
#                 if diff not in mapping[j]:
#                     mapping[i][diff] = 2
#                 else:
#                     mapping[i][diff] = mapping[j][diff] + 1
#                 max_ = max(max_, mapping[i][diff])
            
#         return max_
             
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         track = [0 for i in range(len(A))]
        
#         for i in range(1, len(A)):
#             track[i] = A[i] - A[i-1]
#         print(track)
        
#         num = {}
        
#         for i in range(1, len(track)):
#             val = (track[i] - track[i-1])
#             if val in num:
#                 num[val] += 1
#             else:
#                 num[val] = 1
                
#         print(num)
#         return max(num.values()) + 1
        

