class Solution:
    def getMinArr(self, arr, target, right=False):
        pre_sum = 0
        res = [float('inf') for i in range(len(arr))]
        sum_dict = {0:0}
        if right:
            arr = arr[::-1]
        for i, num in enumerate(arr):
            pre_sum += num
            if i > 0:
                res[i] = res[i-1]
            if pre_sum - target in sum_dict:
                cur_len = i - sum_dict[pre_sum - target] + 1
                res[i] = min(res[i], cur_len)
            sum_dict[pre_sum] = i + 1
        if right:
            res.reverse()
        return res
        
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        left_min = self.getMinArr(arr, target)
        right_min = self.getMinArr(arr, target, True)
        
        min_len = float('inf')
        for i in range(len(arr) - 1):
            min_len = min(min_len, left_min[i] + right_min[i+1])
        if min_len == float('inf'):
            return -1
        return min_len
        
        
        
        
        
        
        
        
#         prefix_sum = [0 for i in range(len(arr) + 1)]
#         for i in range(len(arr)):
#             prefix_sum[i+1] = prefix_sum[i] + arr[i]
            
#         prefix = [float('inf') for i in range(len(arr))]
#         suffix = [float('inf') for i in range(len(arr))]
        
#         for i in range(1, len(arr)):
#             # found = False
#             for j in range(i-1, -1, -1):
#                 if prefix_sum[i] - prefix_sum[j] == target:
#                     # found = True
#                     prefix[i] = i - j
#                     break
        
#         for i in range(len(arr) - 1, -1, -1):
#             # found = False
#             for j in range(i+1, len(arr) + 1):
#                 if prefix_sum[j] - prefix_sum[i] == target:
#                     # found = True
#                     suffix[i] = j - i
#                     break
                
#         for i in range(1, len(prefix)):
#             prefix[i] = min(prefix[i], prefix[i-1])
            
#         for i in range(len(suffix) - 2, -1, -1):
#             suffix[i] = min(suffix[i], suffix[i+1])
            
#         min_len = float('inf')
#         for i in range(len(arr)):
#             min_len = min(min_len, prefix[i] + suffix[i])
#         if min_len == float('inf'):
#             return -1
#         return min_len

