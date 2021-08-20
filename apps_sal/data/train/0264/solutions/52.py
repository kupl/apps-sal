class Solution:

    def maxLength(self, arr):
        prev = {0: 0}
        for word in arr:
            seen = 0
            duplicate = False
            for char in word:
                binaryC = 1 << ord(char) - ord('a')
                if binaryC & seen != 0:
                    duplicate = True
                    break
                else:
                    seen |= binaryC
            if duplicate:
                continue
            toAdd = dict()
            for k in prev:
                if k & seen == 0:
                    toAdd[k | seen] = prev[k] + len(word)
            prev.update(toAdd)
        return max(prev.values())


class Solution:

    def maxLength(self, arr):
        cands = {0: 0}
        for word in arr:
            if len(word) != len(set(word)):
                continue
            currW = sum((1 << ord(char) - ord('a') for char in word))
            toAdd = dict()
            for prevW in cands:
                if prevW & currW == 0:
                    toAdd[prevW + currW] = cands[prevW] + len(word)
            cands.update(toAdd)
        return max(cands.values())
