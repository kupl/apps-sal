class Solution:
    def minOperations(self, nums: List[int]) -> int:
        numOperations = 0
        compare = [0] * len(nums)
        while nums != compare:
            # divByTwo = True
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    nums[i] -= 1
                    numOperations += 1
                    # divByTwo == False
            # if divByTwo:
            if nums == compare:
                return numOperations
            for i in range(len(nums)):
                nums[i] /= 2
            numOperations += 1
            # print(nums)
        return numOperations
