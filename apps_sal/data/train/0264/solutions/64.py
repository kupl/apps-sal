class Solution:
    def maxLength(self, arr: List[str]) -> int:
        N = len(arr)
        charSets = [set()]
        for s in arr:
            currSet = set(s)
            if len(currSet) != len(s):
                continue
            currSize = len(charSets)
            for idx in range(currSize):
                charSet = charSets[idx]
                if charSet & currSet:
                    continue
                charSets.append(charSet | currSet)
        return max(len(charSet) for charSet in charSets)
