class Solution:

    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        ansr = 0
        while any(nums):
            divideByTwo = False
            for i in range(N):
                if nums[i] == 1:
                    ansr += 1
                    nums[i] = 0
                elif nums[i] == 0:
                    continue
                else:
                    divideByTwo = True
                    if nums[i] % 2 == 1:
                        ansr += 1
                    nums[i] = nums[i] // 2
            if divideByTwo:
                ansr += 1
        return ansr
