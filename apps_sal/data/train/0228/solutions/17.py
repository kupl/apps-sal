class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        su, res, vov = 0, 0, ('a', 'e', 'i', 'o', 'u')
        for i, v in enumerate(s):
            if v in vov:
                su += 1
            if i - k >= 0:
                if s[i - k] in vov:
                    su -= 1
            res = max(res, su)
        return res
