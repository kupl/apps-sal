class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        seen_nonzero = True
        while True:
            all_zeros = True
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    ans += 1
                if nums[i] > 0:
                    all_zeros = False

            if all_zeros:
                break

            for i in range(len(nums)):
                nums[i] = nums[i] // 2
            ans += 1
        return ans
