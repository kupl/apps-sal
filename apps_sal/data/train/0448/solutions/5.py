class Solution(object):
    def checkSubarraySum(self, nums, k):

        if k == 0:
            for i in range(0, len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False

        k = abs(k)
        if len(nums) >= k * 2:
            return True

        sum = [0]
        for x in nums:
            sum.append((sum[-1] + x) % k)

        Dict = {}
        for i in range(0, len(sum)):
            if sum[i] in Dict:
                if i - Dict[sum[i]] > 1:
                    return True
            else:
                Dict[sum[i]] = i

        return False
