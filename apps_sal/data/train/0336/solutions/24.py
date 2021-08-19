class Solution:

    def minSteps(self, s: str, t: str) -> int:
        char = {}
        c = 0
        for ch in t:
            if ch not in char.keys():
                char[ch] = 1
            else:
                char[ch] += 1
        for ch in s:
            if ch in char.keys() and char[ch] != 0:
                char[ch] -= 1
            else:
                c += 1
        return c
