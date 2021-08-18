class Solution:
    def stoneGameIII(self, nums: List[int]) -> str:
        n = len(nums)
        total = sum(nums)
        presum = [nums[-1]]
        if n > 1:
            presum.insert(0, nums[-2] + presum[0])
            nums[-2] = max(nums[-2], presum[0])
        if n > 2:
            presum.insert(0, nums[-3] + presum[0])
            nums[-3] = max([nums[-3] + presum[1] - nums[-2], nums[-3] + presum[1] - presum[2], presum[0]])
        for i in range(n - 4, -1, -1):
            get_one = nums[i] + presum[0] - nums[i + 1]
            get_two = nums[i] + presum[0] - presum[1] + presum[1] - nums[i + 2]
            get_three = nums[i] + presum[0] - presum[2] + presum[2] - nums[i + 3]
            presum.pop()
            presum.insert(0, presum[0] + nums[i])
            nums[i] = max([get_one, get_two, get_three])
        if nums[0] == presum[0] / 2:
            return 'Tie'
        elif nums[0] > presum[0] / 2:
            return 'Alice'
        return 'Bob'
