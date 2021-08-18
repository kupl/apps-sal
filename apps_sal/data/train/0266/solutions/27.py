from collections import defaultdict


class Solution:
    def numSplits(self, s: str) -> int:
        rst = 0
        lDict = defaultdict(int)
        rDict = defaultdict(int)

        lDict[s[0]] = 1
        for char in s[1:]:
            rDict[char] += 1

        if(len(rDict) == len(lDict)):
            rst += 1

        for char in s[1:-1]:
            rDict[char] -= 1
            if(rDict[char] == 0):
                rDict.pop(char)
            lDict[char] += 1
            if(len(rDict) == len(lDict)):
                rst += 1
        return rst
