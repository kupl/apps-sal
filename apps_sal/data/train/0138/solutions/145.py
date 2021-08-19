class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        sublists = []
        i = 0
        while nums and i < len(nums):
            if nums[i]:
                i += 1
            else:
                sublists.append(nums[:i])
                nums = nums[i + 1:]
                i = 0
        sublists.append(nums)
        return max([self.getMaxLenFromNonZero(sublist) for sublist in sublists])

    def getMaxLenFromNonZero(self, nums: List[int]) -> int:
        count = 0
        front = len(nums)
        back = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                count += 1
                if front > i:
                    front = i
                back = i
        if count % 2 == 0:
            return len(nums)
        else:
            return len(nums) - min([front + 1, len(nums) - back])
