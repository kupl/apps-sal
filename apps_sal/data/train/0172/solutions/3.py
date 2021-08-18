class Solution:
    def maxDiff(self, num: int) -> int:
        numStr1 = list(str(num))
        numStr2 = list(str(num))
        numStrLen = len(numStr1)
        firstChar = numStr1[0]
        for i, char in enumerate(numStr1):
            if char != firstChar and char > '0':
                for j in range(i, numStrLen):
                    if numStr1[j] == char:
                        numStr1[j] = '0'
                break
            if char == firstChar and char > '1':
                for j in range(i, numStrLen):
                    if numStr1[j] == char:
                        numStr1[j] = '1'
                break
        for i, char in enumerate(numStr2):
            if char < '9':
                for j in range(i, numStrLen):
                    if numStr2[j] == char:
                        numStr2[j] = '9'
                break
        return int(''.join(numStr2)) - int(''.join(numStr1))
