class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return self.dfs(s, 0, [])

    def dfs(self, s, index, ele):
        currMax = 0

        for i in range(index, len(s)):
            if s[index:i + 1] not in ele:
                currMax = max(currMax, 1 + self.dfs(s, i + 1, ele[:] + [s[index:i + 1]]))

        return currMax
