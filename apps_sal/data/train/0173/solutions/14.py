class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        nums = [i % k for i in arr]
        nums = [i for i in nums if i != 0]
        nums.sort()

        if len(nums) % 2 != 0:
            return False

        for i in range(len(nums) // 2):
            if (nums[i] + nums[-1 - i]) % k != 0:
                return False

        return True
