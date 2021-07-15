from collections import defaultdict
class Solution:
    # 先写出brute force solution O(n^2)，在下面
    # 再尝试用dp优化 
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        ret = 0
        
        mappings = defaultdict(list)
        for i, v in enumerate(arr):
            mappings[v].append(i)
            
        M = [-1 for i in range(n)]
        
        def dp(i):
            if i == n-1:
                return 1
            
            if M[i] != -1:
                return M[i]
            
            M[i] = 1
            for j in mappings[arr[i]+difference]:
                if j > i:
                    M[i] += dp(j)
                    break
            
            return M[i]
        
        for i in range(n):
            ret = max(ret, dp(i))
            
        return ret
    
    
#     def longestSubsequence(self, arr: List[int], difference: int) -> int:
#         n = len(arr)
#         ret = 0
        
#         for i, num in enumerate(arr):
#             cur = num
#             length = 1
#             for j in range(i+1, n):
#                 if arr[j] == cur + difference:
#                     length += 1
#                     cur = arr[j]
#             ret = max(ret, length)
        
#         return ret

