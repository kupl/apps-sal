class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxNum = -1
        currNum = 0
        vowels = 'aeiou'
        j = 0
        while j < k:
            if s[j] in vowels:
                currNum += 1
            j += 1
        maxNum = max(maxNum, currNum)

        for i in range(k, len(s)):
            if s[i] in vowels:
                currNum += 1
            if s[i - k] in vowels:
                currNum -= 1

            maxNum = max(maxNum, currNum)

        return maxNum
