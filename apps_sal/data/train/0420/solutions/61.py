class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        d = {0: -1}  # stores binary representation as key for each 0 to i (while i is index in string.)
        binRep = 0
        res = 0  # stores longest substring

        for i, char in enumerate(s):
            if char in vowels:
                binRep = binRep ^ vowels[char]  # toggles the positions.

            if binRep not in d:
                d[binRep] = i
            else:
                res = max(res, i - d[binRep])

        return res
