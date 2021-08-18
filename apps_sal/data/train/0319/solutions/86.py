class Solution:
    def stoneGameIII(self, nums: List[int]) -> str:
        presum = list(itertools.accumulate(nums))

        def sum(i, j):
            if i == 0:
                return presum[j]
            return presum[j] - presum[i - 1]

        n = len(nums)
        if n > 1:
            nums[-2] = max(sum(n - 2, n - 2), sum(n - 2, n - 1))
        if n > 2:
            nums[-3] = max(nums[n - 3] + sum(n - 2, n - 1) - nums[-2], sum(n - 3, n - 2), sum(n - 3, n - 1))
        for i in range(n - 4, -1, -1):
            get_one = nums[i] + sum(i + 1, n - 1) - nums[i + 1]
            get_two = sum(i, i + 1) + sum(i + 2, n - 1) - nums[i + 2]
            get_three = sum(i, i + 2) + sum(i + 3, n - 1) - nums[i + 3]
            nums[i] = max([get_one, get_two, get_three])
        if nums[0] == sum(0, n - 1) / 2:
            return 'Tie'
        elif nums[0] > sum(0, n - 1) / 2:
            return 'Alice'
        return 'Bob'
