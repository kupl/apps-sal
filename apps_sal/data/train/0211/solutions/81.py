class Solution:

    def helper(self, s, occur):
        if len(s) == 0:
            return 0
        curMax = -1
        for i in range(1, len(s) + 1):
            if s[:i] not in occur:
                occur.append(s[:i])
                if (s[i:], tuple(occur)) in self.memo:
                    res = self.memo[s[i:], tuple(occur)]
                else:
                    res = self.helper(s[i:], occur)
                    self.memo[s[i:], tuple(occur)] = res
                if res >= 0:
                    curMax = max(curMax, 1 + res)
                occur.pop()
        return curMax

    def maxUniqueSplit(self, s: str) -> int:
        self.memo = {}
        return self.helper(s, [])
