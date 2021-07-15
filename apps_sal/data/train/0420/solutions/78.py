class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = 'aeiou'
        helper = {0: -1}
        state = 0
        res = 0
        for i, ch in enumerate(s):
            j = vowels.find(ch)
            if j >= 0:
                state ^= 1 << j
            if state not in helper:
                helper[state] = i
            res = max(res, i - helper[state])
        return res
                
            

