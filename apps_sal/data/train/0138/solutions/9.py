class Solution:

    def getMaxLen(self, nums: List[int]) -> int:

        def solve(nums):
            cnt = 0
            for n in nums:
                if n < 0:
                    cnt += 1
            if cnt % 2 == 0:
                return len(nums)
            for i in range(len(nums)):
                if nums[i] < 0:
                    first = i
                    break
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] < 0:
                    last = i
                    break
            return max(last, len(nums) - first - 1)
        l = 0
        ans = 0
        nums.append(0)
        for r in range(len(nums)):
            if nums[r] == 0:
                cur = solve(nums[l:r])
                ans = max(ans, cur)
                l = r + 1
        return ans
