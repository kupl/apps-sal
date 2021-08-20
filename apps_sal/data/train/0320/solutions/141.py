class Solution:

    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while True:
            Zero = True
            for i in range(len(nums)):
                if nums[i] & 1:
                    nums[i] -= 1
                    count += 1
                if nums[i]:
                    Zero = False
            if Zero:
                return count
            count += 1
            for i in range(len(nums)):
                nums[i] >>= 1
