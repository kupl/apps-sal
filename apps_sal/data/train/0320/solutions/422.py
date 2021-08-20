class Solution:

    def minOperations(self, nums: List[int]) -> int:
        count = 0
        numzeros = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                numzeros += 1
        while numzeros < n:
            k = 0
            for i in range(n):
                if nums[i] % 2:
                    nums[i] -= 1
                    count += 1
                    if nums[i] == 0:
                        numzeros += 1
                    else:
                        k = 1
                        nums[i] = nums[i] / 2
                elif nums[i] == 0:
                    continue
                else:
                    k = 1
                    nums[i] = nums[i] / 2
            if k == 1:
                count += 1
        return count
