class Solution:
    def checkSubarraySum(self, nums, k):
        dict, cur = {}, 0
        if k == 0:
            zero = 0
            for i in nums:
                if i == 0 and zero == 1:
                    return True
                elif i == 0 and zero != 1:
                    zero = 1
                else:
                    zero = 0
            return False
        for i in range(len(nums)):
            cur += nums[i]
            if i != 0 and cur % k == 0:
                print('1')
                return True
            elif cur % k in dict and cur >= k:
                print('2')
                return True
            elif i != 0 and nums[i] == 0 and nums[i - 1] == 0:
                print('3')
                return True
            else:
                dict[cur % k] = True
        return False
        """
         :type nums: List[int]
         :type k: int
         :rtype: bool
         """
