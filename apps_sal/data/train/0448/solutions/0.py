class Solution:

    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            j = 0
            for i in range(0, len(nums)):
                if nums[i] == 0:
                    if j < i:
                        return True
                else:
                    j = i + 1
            return False
        dic = {0: -1}
        c = 0
        for i in range(0, len(nums)):
            c = (c + nums[i]) % k
            if c in dic:
                if i - dic[c] > 1:
                    return True
            else:
                dic[c] = i
        return False
