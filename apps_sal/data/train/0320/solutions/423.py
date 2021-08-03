class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = 1
        count = 0
        maxn = max(nums)
        while c * 2 <= maxn:
            c = c * 2
            count += 1

        @lru_cache
        def dfs(n):
            if n <= 1:
                return n
            else:
                if n % 2 == 0:
                    return dfs(n // 2)
                else:
                    return 1 + dfs(n // 2)
        for i in nums:
            count += dfs(i)
        return count
