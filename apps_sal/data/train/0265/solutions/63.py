class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefix = list(itertools.accumulate(nums))

        def dfs(i):
            s = {prefix[i - 1] if i > 0 else 0}
            for j in range(i, len(prefix)):
                if prefix[j] - target in s:
                    return 1 + dfs(j + 1)
                s.add(prefix[j])
            return 0

        return dfs(0)
