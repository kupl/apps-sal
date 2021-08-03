class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 0
        vowelString = ['a', 'e', 'i', 'o', 'u']
        end = 0
        start = 0
        maxx = 0
        while end < len(s):
            if s[end] in vowelString:
                vowels += 1

            if end >= k:
                if s[start] in vowelString:
                    vowels -= 1
                start += 1
            end += 1
            maxx = max(maxx, vowels)
        return maxx
