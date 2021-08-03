class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        i, tmp, res = 0, 0, 0
        for j in range(len(s)):
            if s[j] in vowels:
                tmp += 1
            while j - i + 1 > k:
                if s[i] in vowels:
                    tmp -= 1
                i += 1
            res = max(res, tmp)

        return res
