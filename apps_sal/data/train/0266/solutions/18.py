class Solution:

    def numSplits(self, s: str) -> int:
        characters = []
        possibleSplits = 0
        for i in range(len(s)):
            if s[i] not in characters:
                characters.append(s[i])
        for i in range(len(s)):
            leftChars = 0
            rightChars = 0
            leftSide = s[:i]
            rightSide = s[i:]
            for j in range(len(characters)):
                if characters[j] in leftSide:
                    leftChars += 1
                if characters[j] in rightSide:
                    rightChars += 1
            if leftChars == rightChars:
                possibleSplits += 1
        return possibleSplits
