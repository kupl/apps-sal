class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bits = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        seen = {0: -1}
        max_val = 0
        cur = 0
        for i, char in enumerate(s):
            if char in bits:
                cur ^= bits[char]
            seen.setdefault(cur, i)
            max_val = max(max_val, i - seen[cur])

        return max_val
