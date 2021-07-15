class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        start = 0
        ans = 0
        cur = 0
        for end in range(len(s)):  
            val = abs(ord(s[end]) - ord(t[end]))
            cur += val
            if cur <= maxCost:
                ans = max(ans, end-start+1)
            else:
                while cur > maxCost:
                    cur -= abs(ord(s[start]) - ord(t[start]))
                    start += 1
                
        return ans
