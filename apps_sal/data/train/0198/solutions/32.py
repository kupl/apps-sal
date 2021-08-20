class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maxLength = 0
        currLength = 0
        currCost = 0
        for i in range(len(s)):
            currLength += 1
            currCost += abs(ord(s[i]) - ord(t[i]))
            while currCost > maxCost:
                currCost -= abs(ord(s[i - (currLength - 1)]) - ord(t[i - (currLength - 1)]))
                currLength -= 1
            maxLength = max(maxLength, currLength)
        return maxLength
