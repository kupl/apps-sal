class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
#         indices = []
#         for i,v in enumerate(nums):
#             if v == 1:
#                 indices.append(i)
#         diffs = []
#         for i in range(1, len(indices)):
#             diffs.append(indices[i] - indices[i -1] - 1)
        
#         return all([x >= k for x in diffs])
        prev_one_ind = -1
        for i,v in enumerate(nums):
            if v == 1:
                if prev_one_ind >= 0:
                    diff = i - prev_one_ind - 1
                    if diff < k:
                        return False
                prev_one_ind = i
                    
        return True
