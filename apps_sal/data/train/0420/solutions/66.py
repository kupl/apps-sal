class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        res = 0
        pos = {0: -1}
        state = 0
        vowels = 'aeiou'
        for i in range(len(s)):
            j = vowels.find(s[i])
            if j >= 0:
                state ^= 1 << j
            if state in pos:
                res = max(res, i - pos[state])
            else:
                pos[state] = i
        return res
