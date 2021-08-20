class Solution:

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        while True:
            for i in range(n):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    ans += 1
            all_zeros = True
            for i in range(n):
                if nums[i] != 0:
                    all_zeros = False
                nums[i] = nums[i] // 2
            if all_zeros:
                break
            else:
                ans += 1
        return ans
