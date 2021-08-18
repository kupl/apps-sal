class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        d = {0: -1}
        binRep = 0
        res = 0

        for i, char in enumerate(s):
            if char in vowels:
                binRep = binRep ^ vowels[char]

            if binRep not in d:
                d[binRep] = i
            else:
                res = max(res, i - d[binRep])

        return res
