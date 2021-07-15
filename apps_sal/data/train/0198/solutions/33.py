class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = 0
        i,j = 0,0
        while j < len(s):
            maxCost -= abs(ord(t[j]) - ord(s[j]))
            while maxCost < 0:
                maxCost += abs(ord(t[i]) - ord(s[i]))
                i += 1
            j += 1
            res = max(res, j -i)
        return res
