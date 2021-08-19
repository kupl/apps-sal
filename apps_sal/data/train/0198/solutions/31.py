class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        currCost = 0
        maxLength = 0
        start = 0
        curr = 0
        while curr < len(s):
            currCost += abs(ord(s[curr]) - ord(t[curr]))
            while currCost > maxCost:
                currCost = currCost - abs(ord(s[start]) - ord(t[start]))
                start += 1
            if curr - start + 1 > maxLength:
                maxLength = curr - start + 1
            curr += 1
        return maxLength
