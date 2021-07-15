# n^2 time to look at all subarrays
# n time to iterate backwards ?
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        min_right = min(A)
        max_left = 0
        
        min_from_right = []
        current_min_right = A[-1]
        for i in range(len(A) - 1, -1, -1):
            current_min_right = min(A[i], current_min_right)
            min_from_right.insert(0, current_min_right)
        
        for i in range(len(A)):
            current = A[i]
            max_left = max(max_left, current)
            min_right = min_from_right[i + 1] if i < len(A) else 0
            if max_left <= min_right:
                return i + 1

#         def check_partitions(a, b):
#             max_a = 0
#             for num in a:
#                 max_a = max(max_a, num)
#             min_b = maxsize
#             for num in b:
#                 min_b = min(min_b, num)
#             if max_a <= min_b and len(a) > 0 and len(b) > 0:
#                 return len(a)
#             return -1
        
#         min_left = maxsize
#         for i in range(1, len(A) + 1):
#             cand = check_partitions(A[0:i], A[i: len(A)])
#             if cand != -1:
#                 min_left = min(min_left, cand)
        
#         return min_left

