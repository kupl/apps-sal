class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        ref = [0] * N
        res = 0
        while nums != ref:
            isAllEven = 1
            for i in range(N):
                if nums[i] % 2:
                    nums[i] -= 1
                    res += 1
                    isAllEven = 0
            if isAllEven:
                for i in range(N):
                    nums[i] //= 2
                res += 1
            # print(nums, res)
        return res
