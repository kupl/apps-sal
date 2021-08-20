class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while True:
            maxv = 0
            for k in range(len(nums)):
                if nums[k] % 2:
                    nums[k] -= 1
                    ans += 1
                maxv = max(maxv, nums[k])
            if maxv == 0:
                break
            if maxv > 0:
                for k in range(len(nums)):
                    nums[k] //= 2
                ans += 1
        return ans
