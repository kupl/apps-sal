class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        currcost = 0
        i = 0
        j = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            if abs(ord[s[0]]) - ord(t[0]) >= maxcost:
                return 1
            else:
                return 0
        currcost = 0
        ans = 0
        state = False
        while i < len(s) and j < len(s):
            if currcost + abs(ord(s[j]) - ord(t[j])) <= maxCost:
                currcost += abs(ord(s[j]) - ord(t[j]))
                j += 1
                state = True
            else:
                ans = max(ans, j - i)
                currcost -= abs(ord(s[i]) - ord(t[i]))
                i += 1
                state = False
                if i >= j:
                    j = i
                    currcost = 0
        if state:
            ans = max(ans, j - i)
        return ans
