class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        if s % 3 == 0:
            return s
        pos_1_1, pos_2_1 = True, True
        min_1_1, min_1_2, min_2_1, min_2_2 = float('inf'), float('inf'), float('inf'), float('inf')
        for i in range(n):
            if nums[i] % 3 == 1:
                if nums[i] < min_1_1:
                    min_1_1 = nums[i]
                    pos_1_1 = i
            elif nums[i] % 3 == 2:
                if nums[i] < min_2_1:
                    min_2_1 = nums[i]
                    pos_2_1 = i
        for i in range(n):
            if i == pos_1_1 or i == pos_2_1:
                continue
            if nums[i] % 3 == 1:
                min_1_2 = min(min_1_2, nums[i])
            if nums[i] % 3 == 2:
                min_2_2 = min(min_2_2, nums[i])

        if s % 3 == 1:
            return s - min(min_1_1, min_2_1 + min_2_2)
        return s - min(min_2_1, min_1_1 + min_1_2)
