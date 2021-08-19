class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        ret = 0

        def backtrack(start, currSet):
            if start == len(s):
                nonlocal ret
                ret = max(ret, len(currSet))
                return
            for i in range(start, len(s)):
                if s[start:i + 1] not in currSet:
                    currSet.add(s[start:i + 1])
                    backtrack(i + 1, currSet)
                    currSet.remove(s[start:i + 1])
        backtrack(0, set())
        return ret
