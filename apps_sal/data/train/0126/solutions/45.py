class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        maxi = 0

        for index in range(minSize, maxSize + 1):
            result = self.getAllSubstringsWithRules(s, maxLetters, index)

            if result > maxi:
                maxi = result

        return maxi

    def getAllSubstringsWithRules(self, s, maxLetters, size):
        length = len(s)
        letters = {}
        subStrings = {}

        for index in range(size):
            letter = s[index]

            if letter not in letters:
                letters[letter] = 0

            letters[letter] += 1

        if len(letters) <= maxLetters:
            subStrings[s[:size]] = 1

        for index in range(size, length):
            letterToRemove = s[index - size]
            letters[letterToRemove] -= 1

            if letters[letterToRemove] == 0:
                del letters[letterToRemove]

            letterToAdd = s[index]

            if letterToAdd not in letters:
                letters[letterToAdd] = 0

            letters[letterToAdd] += 1

            if len(letters) <= maxLetters:
                string = s[index - size + 1:index + 1]
                if string not in subStrings:
                    subStrings[string] = 0

                subStrings[string] += 1

        if not subStrings:
            return 0

        return max(subStrings.values())
