class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_length = 0
        start = 0
        end = 0
        cost = 0
        while end < len(s):
            c = abs(ord(s[end]) - ord(t[end]))
            if cost + c <= maxCost:
                cost += c
                end += 1
            else:
                cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            max_length = max(max_length, end - start) 
        return max_length 

