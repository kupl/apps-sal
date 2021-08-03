class Solution:
    p1dict = {}
    p2dict = {}

    def play1(self, nums):
        if str(nums) in self.p1dict:
            return self.p1dict[str(nums)]
        if len(nums) == 1:
            return nums[0]
        ret = max(self.play2(nums[1:]) + nums[0], self.play2(nums[:-1]) + nums[-1])
        self.p1dict[str(nums)] = ret
        return ret

    def play2(self, nums):
        if str(nums) in self.p2dict:
            return self.p2dict[str(nums)]
        if len(nums) == 1:
            return -nums[0]
        ret = min(self.play1(nums[1:]) - nums[0], self.play1(nums[:-1]) - nums[-1])
        self.p2dict[str(nums)] = ret
        return ret

    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.play1(nums) >= 0
