class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        masks = {'a': 16, 'e': 8, 'i': 4, 'o': 2, 'u': 1}
        num = 0
        numToIdx = {0: -1}
        ans = 0
        for i, ch in enumerate(s):
            if ch in masks:
                num ^= masks[ch]
            if num not in numToIdx:
                numToIdx[num] = i
            ans = max(ans, i - numToIdx[num])
        return ans
