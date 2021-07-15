class Solution:
    def maxLength(self, arr: List[str]) -> int:
        N = len(arr)
        # store the intermediate sets of unique characters
        charSets = [set()]
        # iterate over each string
        for s in arr:
            # iterate over each char set to see if we can add the chars in s into it
            currSet = set(s)
            # skip string swith duplicate chars
            if len(currSet) != len(s):
                continue
            currSize = len(charSets)
            for idx in range(currSize):
                charSet = charSets[idx]
                # check if the sets have an intersection (duplicate chars)
                if charSet & currSet:
                    continue
                charSets.append(charSet | currSet)
        return max(len(charSet) for charSet in charSets)
