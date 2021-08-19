class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = curr = i = j = 0
        while i < len(s) and j < len(s):
            curr += abs(ord(s[j]) - ord(t[j]))
            j += 1
            while curr > maxCost:
                curr -= abs(ord(s[i]) - ord(t[i]))
                i += 1
            res = max(res, j - i)
        return res
