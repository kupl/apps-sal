class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0
        mp = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        seen = [len(s)] * 63
        seen[0] = -1
        max_len = 0
        for i in range(len(s)):
            if s[i] in 'aeiou':
                mask ^= (1 << mp[s[i]])
            seen[mask] = min(seen[mask], i)
            max_len = max(max_len, i - seen[mask])
        return max_len
