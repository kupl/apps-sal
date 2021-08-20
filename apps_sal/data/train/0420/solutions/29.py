class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        current = [0, 0, 0, 0, 0]

        def convertToInteger():
            nonlocal current
            binarySum = 0
            for num in current:
                binarySum *= 2
                binarySum += num
            return binarySum

        def incrementVowels(char):
            nonlocal current
            if char == 'a':
                current[0] = 1 - current[0]
            elif char == 'e':
                current[1] = 1 - current[1]
            elif char == 'i':
                current[2] = 1 - current[2]
            elif char == 'o':
                current[3] = 1 - current[3]
            elif char == 'u':
                current[4] = 1 - current[4]
        earliest = {}
        earliest[0] = -1
        maxLength = 0
        current = [0, 0, 0, 0, 0]
        for (index, char) in enumerate(s):
            incrementVowels(char)
            binarySum = convertToInteger()
            if binarySum not in earliest:
                earliest[binarySum] = index
            else:
                maxLength = max(index - earliest[binarySum], maxLength)
        return maxLength
