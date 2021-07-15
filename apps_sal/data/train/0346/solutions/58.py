class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [n % 2 for n in nums]
        
        def atMost(k):
            ans, j = 0, 0
            for i, n in enumerate(nums):
                k -= n
                while k < 0:
                    k += nums[j]
                    j += 1
                ans += i - j + 1
            return ans
        
        return atMost(k) - atMost(k - 1)
        
        
        
#         ans, i, j, cnt = 0, 0, 0, 0
#         for i, n in enumerate(nums):
#             cnt += nums[i]
#             if cnt == k:
#                 if nums[i]:
#                     cur = nums[j:].index(1)
#                 ans += cur + 1
#             elif cnt > k:
#                 j += cur + 1
#                 cnt -= 1
#                 cur = nums[j:].index(1)
#                 ans += cur + 1
#         return ans
        
        
#         def atMost(k):
#             res = i = 0
#             for j in xrange(len(A)):
#                 k -= A[j] % 2
#                 while k < 0:
#                     k += A[i] % 2
#                     i += 1
#                 res += j - i + 1
#             return res

#         return atMost(k) - atMost(k - 1)

