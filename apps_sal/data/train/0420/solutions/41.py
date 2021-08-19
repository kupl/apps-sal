class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        first_position = {0: -1}
        bit_ind = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        ans = key = 0
        for (i, c) in enumerate(s):
            if c in bit_ind:
                key = key ^ 1 << bit_ind[c]
            if key not in first_position:
                first_position[key] = i
            ans = max(i - first_position[key], ans)
        return ans
