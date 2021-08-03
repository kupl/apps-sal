class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        i = 0
        res = 0
        while i < k:
            if s[i] in vowel:
                res += 1
            i += 1
        j = k
        i = 0
        maxV = res
        while j < n:
            if s[i] in vowel:
                res -= 1
            if s[j] in vowel:
                res += 1
            i += 1
            j += 1
            if maxV < res:
                maxV = res
        return maxV
