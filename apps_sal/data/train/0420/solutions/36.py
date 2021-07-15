class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        seen = {(0, 0, 0, 0, 0): -1}
        counts = {c:0 for c in 'aeiou'}
        res = 0
        for i, ch in enumerate(s):
            if ch in counts:
                counts[ch] += 1
            key = tuple([counts[c]%2 for c in 'aeiou'])
            seen.setdefault(key, i)
            res = max(res, i-seen[key])
        return res

