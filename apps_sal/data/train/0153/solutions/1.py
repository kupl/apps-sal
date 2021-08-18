class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        total = sum(nums)
        if total % 4 != 0 or len(nums) < 4:
            return False
        size = total / 4
        nums.sort(reverse=True)
        used = [False] * len(nums)

        def dfs(i, expect):
            if i >= len(nums):
                return expect % size == 0
            if used[i]:
                return dfs(i + 1, expect)
            used[i] = True
            if nums[i] == expect:
                return True
            if nums[i] < expect:
                expect -= nums[i]
                available = [j for j in range(i + 1, len(nums)) if not used[j]]
                for x in available:
                    if dfs(x, expect):
                        return True
            used[i] = False
            return False
        for i in range(len(nums)):
            if not dfs(i, size):
                return False
        return True
