class Solution:

    def minOperations(self, nums: List[int]) -> int:
        m = 0
        numb = len(nums)
        while True:
            zc = 0
            var = 0
            for i in range(numb):
                if nums[i] % 2 != 0:
                    nums[i] = nums[i] - 1
                    m += 1
                if nums[i] == 0:
                    zc += 1
            if zc == numb:
                break
            nums = list([i // 2 for i in nums])
            m += 1
        return m
