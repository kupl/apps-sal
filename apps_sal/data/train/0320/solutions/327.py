class Solution:

    def minOperations(self, nums: List[int]) -> int:
        lim = len(nums)
        test = [0] * lim
        t = 0
        while nums != test:
            vals = []
            v = 0
            for i in range(0, lim):
                if nums[i] % 2 == 0:
                    vals.append(nums[i] // 2)
                else:
                    nums[i] -= 1
                    v += 1
            if v == 0:
                nums = vals
                t += 1
            else:
                t += v
        return t
