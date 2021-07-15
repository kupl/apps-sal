class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        if n == 1:
            return A[0]
        
        max_ = A[0]
        current = 0
        for num in A:
            current += num
            max_ = max(max_, current)
            if current < 0:
                current = 0
        
        max_from_left = [0] * n
        max_from_left[0] = float('-inf')
        current = A[0]
        for idx in range(1, n):
            max_from_left[idx] = max(max_from_left[idx - 1], current)
            current += A[idx]
        max_from_left[0] = 0
        
        so_far = 0
        for idx in range(n - 1, -1, -1):
            so_far += A[idx]
            max_ = max(max_, so_far + max_from_left[idx])
        return max_
        
#         left_acc = [0] * n
#         left_acc[0] = A[0]
#         for idx in range(1, n):
#             left_acc[idx] = A[idx] + left_acc[idx - 1]
            
        
#         right_acc = [0] * n
#         right_acc[-1] = A[-1]
#         for idx in range(n - 2, -1, -1):
#             right_acc[idx] = A[idx] + right_acc[idx + 1]
        
#         print(left_acc)
#         print(right_acc)
#         left, right = 0, n - 1
#         while left < right:
#             max_ = max(max_, left_acc[left] + right_acc[right])
#             if left_acc[left] > right_acc[right]:
#                 right -= 1
#             else:
#                 left += 1
        
#         return max_

