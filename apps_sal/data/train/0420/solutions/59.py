class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        masks = {0: -1}
        mask = 0
        match = {
            'a' : 1,
            'e' : 2,
            'i' : 4,
            'o' : 8,
            'u': 16
        }
        max_len = 0
        for i, ch in enumerate(s):
            if ch in match:
                mask = mask ^ (1 << match[ch])
            if mask in masks:
                max_len = max(max_len, i - masks[mask])
            else:
                masks[mask] = i
        return max_len
