class Solution:

    def maxUniqueSplit(self, s: str) -> int:

        def check(s):
            if len(s) == 1:
                return [[s]]
            if len(s) == 0:
                return [[]]
            ans = []
            for i in range(1, len(s) + 1):
                for item in check(s[i:]):
                    ans.append([s[:i]] + item)
            return ans
        result = check(s)
        ans = 0
        for item in result:
            if len(set(item)) == len(item):
                ans = max(len(item), ans)
        return ans
