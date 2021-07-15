class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        
        def lcs_helper(index1, index2, memo = {}):
        
            if index1 == len(text1) or index2 == len(text2):
                return 0
            key = (index1, index2)
            if key not in memo:

                if text1[index1] == text2[index2]:
                    memo[key] = 1 + lcs_helper(index1+1, index2+1, memo)
                else:
                    memo[key] =  max(lcs_helper(index1, index2+1,memo),
                           lcs_helper(index1+1, index2, memo))
            return memo[key]
        
        return lcs_helper(0,0)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         max_count = float(\"-inf\")
        
#         for _ in range(len(text1)):
#             curr_count = 0
#             left_index = 0
#             for index in range(_,len(text1)):
#                 char = text1[index]
#                 if text2.find(char, left_index) != -1:
#                     curr_count +=1
#                     left_index = text2.find(char, left_index) + 1
#                     remaining_string = text2[left_index:]
#             max_count = max(max_count, curr_count)
                
#         return max_count
                
                

