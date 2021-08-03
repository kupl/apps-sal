class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        minV = nums[0]
        maxV = nums[0]
        for i in range(len(nums)):
            if nums[i] < minV:
                minV = nums[i]
            if nums[i] > maxV:
                maxV = nums[i]

        l = len(nums)
        n_size = max((maxV - minV) // (l - 1), 1)
        # print(n_size)
        n = (maxV - minV) // n_size + 1
        # print(n)
        # return 0
        if n == 1:
            return maxV - minV

        b_max = [minV] * n
        b_min = [maxV] * n
        b_count = [0] * n

        for i in range(l):
            b_id = (nums[i] - minV) // n_size
            b_count[b_id] += 1
            if nums[i] > b_max[b_id]:
                b_max[b_id] = nums[i]
            if nums[i] < b_min[b_id]:
                b_min[b_id] = nums[i]

        last_max = minV
        maxGap = 1
        for i in range(n):
            if b_count[i] > 0:
                maxGap = max(maxGap, b_min[i] - last_max)
                last_max = b_max[i]

        return maxGap
