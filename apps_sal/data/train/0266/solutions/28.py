import collections


class Solution:
    def numSplits(self, s: str) -> int:
        leftMap = collections.defaultdict(int)
        rightMap = collections.defaultdict(int)

        for ch in s:
            rightMap[ch] += 1

        output = 0

        for ch in s:
            rightMap[ch] -= 1
            if rightMap[ch] == 0:
                del rightMap[ch]

            leftMap[ch] += 1

            if len(rightMap) == len(leftMap):
                output += 1
        return output
