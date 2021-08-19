class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                sub = s[j:j + i]
                has_odd_vowel = False
                for vowel in ['a', 'e', 'i', 'o', 'u']:
                    if sub.count(vowel) % 2 != 0:
                        has_odd_vowel = True
                        break
                if not has_odd_vowel:
                    return i
        return 0
