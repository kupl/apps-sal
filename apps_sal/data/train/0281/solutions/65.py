class Solution:

    def getMoves(self, cFrom, cTo):
        return (ord(cTo) - ord(cFrom)) % 26

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        usedDict = {}
        for (cFrom, cTo) in zip(s, t):
            if cFrom == cTo:
                continue
            moves = self.getMoves(cFrom, cTo)
            if moves > k:
                return False
            if moves not in usedDict:
                usedDict[moves] = 1
            elif moves + 26 * usedDict[moves] <= k:
                usedDict[moves] += 1
            else:
                return False
        return True
