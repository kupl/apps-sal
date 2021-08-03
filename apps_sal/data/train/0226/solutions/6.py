class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        # nums.sort()
        self.ans = 0

        def isSquare(v):
            x = int(v**0.5)
            return x * x == v

        def dfs(pos):

            if pos >= len(nums):
                self.ans += 1
                return

            used = set()
            for i in range(pos, len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                nums[pos], nums[i] = nums[i], nums[pos]

                if (pos == 0) or (pos > 0 and isSquare(nums[pos] + nums[pos - 1])):
                    dfs(pos + 1)
                nums[pos], nums[i] = nums[i], nums[pos]
        dfs(0)
        return self.ans
