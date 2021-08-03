class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        N3 = N / 3
        nums.sort()
        result = []
        if N < 1:
            return nums

        _cnt = 0
        _num = nums[0]

        for n in nums:
            if n != _num:
                if _cnt > N3:
                    result.append(_num)
                _cnt = 1
                _num = n
            else:
                _cnt += 1
        else:
            if _cnt > N3:
                result.append(_num)

        return result
