class Solution:
    # brute force
#     def longestSubsequence(self, arr: List[int], difference: int) -> int:
#         ret = 0
#         for i in range(len(arr)):
#             n = 1
            
#             start = arr[i]
#             j = i + 1
#             while j < len(arr):
#                 if arr[j] - start == difference:
#                     n += 1
#                     start = arr[j]
#                 j += 1
                    
#             ret = max(ret, n)
                
                
                
#         return ret

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        d = dict() # k=last, value=chain
        ret = 0
        for i,n in enumerate(arr):
            if n - difference not in d:
                d[n] = 1
            else:
                d[n] = d[n-difference] + 1
                
            ret = max(ret, d[n])
        return ret
            
            

