class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        digits = {c: i for i, c in enumerate('aeiou')}
        ans = counter = 0
        seen = {0: -1}
        for i, c in enumerate(s):
            if c in digits:
                counter ^= 1 << digits[c]
            seen.setdefault(counter, i)
            ans = max(ans, i - seen[counter]) 
        return ans

