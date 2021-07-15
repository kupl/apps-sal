class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        #3:57pm
        
        
        # first sort it, then use two pointer
        
#         nums.sort()
#         l, r = 0, len(nums)-1
#         res = 0
#         stack = []
        
#         while l <= r and not stack:
#             sums = nums[l] + nums[r]
#             if sums <= target:
#                 stack.append((l, r))
#                 break
#             r -= 1
        
#         while stack:
#             l, r = stack.pop()
#             res += r - l + 1
#             l += 1
#             if l < r and nums[l] + nums[r] <= target:
#                 stack.append((l, r))
#             elif l == r-1 and nums[l] + nums[r] > target:
#                 res += 1
#                 break
                
#         return res

        A = nums
        A.sort()
        l, r = 0, len(A) - 1
        res = 0
        mod = 10**9 + 7
        while l <= r:
            if A[l] + A[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, mod)
                l += 1
        return res % mod
