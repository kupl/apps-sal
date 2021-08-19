class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = 0
        while (True):
            zero_count = 0
            i = 0
            # for i in range(n):
            while i < n:
                if nums[i] % 2 == 1:  # first odd num
                    break
                elif nums[i] == 0:
                    zero_count += 1
                i += 1

            if zero_count == n:
                return ans

            if i == n:
                for j in range(n):
                    nums[j] //= 2
                ans += 1

            for j in range(i, n):
                if nums[j] % 2 == 1:
                    nums[j] -= 1
                    ans += 1

        return ans
#         ans = 0
#         n = len(nums)
#         zeros = len([i==0 for i in nums])
#         if n==zeros: return ans
#         for i in range(n):
#             if nums[i]%2==1: # convert odd to even num
#                 ans+=1
#                 nums[i]-=1
#                 if nums[i]==0:
#                     zeros+=1
#         if n==zeros: return ans

#         while zeros<n:
#             for i in range(n):
#                 nums[i]//=2
#             ans+=1
#         return ans
