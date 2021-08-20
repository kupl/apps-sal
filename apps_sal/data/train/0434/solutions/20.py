class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        groups = [[k, len(list(g))] for (k, g) in itertools.groupby(nums)]
        if len(groups) == 1:
            return groups[0][1] - 1 if groups[0][0] else 0
        ans = 0
        for i in range(len(groups)):
            (k, klen) = groups[i]
            if k:
                ans = max(ans, klen)
            elif i not in [0, len(groups) - 1] and klen == 1:
                ans = max(ans, groups[i - 1][1] + groups[i + 1][1])
        return ans
