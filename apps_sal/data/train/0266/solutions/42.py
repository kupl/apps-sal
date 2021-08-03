class Solution:
    def numSplits(self, s: str) -> int:
        leftCount = collections.Counter()
        rightCount = collections.Counter(s)

        res = 0
        for c in s:
            leftCount[c] += 1
            rightCount[c] -= 1
            if rightCount[c] == 0:
                del rightCount[c]
            if len(rightCount) == len(leftCount):
                res += 1
        return res
