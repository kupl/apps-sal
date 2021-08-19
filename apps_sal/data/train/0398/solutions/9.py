class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if sum(nums[i:j+1]) == k:
        #             count += 1
        # return count

#         count = 0
#         s = 0
#         cum_sum = []
#         for x in nums:
#             s += x
#             cum_sum.append(s)
#             if s == k:
#                 count += 1

#         for i,x in enumerate(cum_sum):
#             for y in cum_sum[i+1:]:
#                 if y - x == k:
#                     count += 1
#         return count

        # good answer @awice
        # time: O(n) space: O(1)
        # idea:count[V] is the number of previous prefix sums with value V. If our newest prefix sum has value W, and W-V == K,
        #   then we add count[V] to our answer.This is because at time t, A[0] + A[1] + ... + A[t-1] = W,
        #   and there are count[V] indices j with j < t-1 and A[0] + A[1] + ... + A[j] = V.
        #   Thus, there are count[V] subarrays A[j+1] + A[j+2] + ... + A[t-1] = K.
        count = collections.Counter()
        count[0] = 1
        ans = su = 0
        for x in nums:
            su += x
            ans += count[su - k]
            count[su] += 1
        return ans
