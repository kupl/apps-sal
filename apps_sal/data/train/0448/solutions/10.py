class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = 0
        dic = collections.defaultdict(list)
        dic[0].append(-1)

        for i in range(0, len(nums)):
            s += nums[i]
            if k == 0:
                dic[s].append(i)
                if i - dic[s][0] > 1:
                    return True
            else:
                dic[s % k].append(i)
                if i - dic[s % k][0] > 1:
                    return True

        return False
