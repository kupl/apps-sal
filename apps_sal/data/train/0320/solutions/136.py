class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        all_zero = False
        while not all_zero:
            all_zero = True
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    ans += 1
                    nums[i] -= 1
                nums[i] //= 2
                if nums[i] != 0:
                    all_zero = False
            if not all_zero:
                ans += 1
        return ans
