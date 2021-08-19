from collections import Counter


class Solution:

    def numSplits(self, s: str) -> int:
        rightS = Counter(s)
        leftS = Counter()
        count = 0
        for c in s:
            leftS[c] += 1
            rightS[c] -= 1
            if rightS[c] == 0:
                del rightS[c]
            count += len(leftS.keys()) == len(rightS.keys())
        return count
