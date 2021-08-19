"""
asdadrwsg3234
   l
     r
"""


class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        vo = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        (l, max_l, count) = (0, 0, 0)
        for i in range(len(s)):
            ch = s[i]
            if ch in vo:
                count += 1
            if i - l + 1 > k:
                if s[l] in vo:
                    count -= 1
                l += 1
            max_l = max(max_l, count)
        return max_l
