class Solution:

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return 0
        s = 0
        e = 0
        step = 0
        while e < len(nums) - 1:
            fst = e
            step += 1
            for i in range(s, e + 1):
                if fst < nums[i] + i:
                    fst = nums[i] + i
            s = e + 1
            e = fst
        return step
