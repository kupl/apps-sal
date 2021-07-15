class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        cnt = collections.Counter()
        cnt[0] = 0
        ans = 0
        prefix = 0
        for n in nums:
            prefix += n
            # if p
            if prefix-target in cnt:
                ans += 1
                cnt = collections.Counter()
            cnt[prefix] += 1
            # print(cnt, ans)
        # print('--')
        return ans
    
    
#         dic = {0:0}
#         ans = 0
#         sum = 0
#         for i in range(len(nums)):
#             sum+=nums[i]
#             if sum-target in dic:
#                 ans+=1
#                 dic = {}
#             dic[sum] = i
#         return ans

