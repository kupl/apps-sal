class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)

        self.res = 0

        def helper(curIdx, curW, curSets):
            if (curIdx == n):
                self.res = max(self.res, len(curSets))
                return

            # don't split
            helper(curIdx + 1, curW + s[curIdx], curSets)

            # split
            if (curW + s[curIdx] not in curSets):
                helper(curIdx + 1, '', curSets | {(curW + s[curIdx])})

        helper(0, '', set())

        return self.res
