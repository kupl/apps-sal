class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        (mx, vowelCount) = (0, 0)
        (l, r) = (0, 0)
        while r < len(s):
            if s[r] in vowels:
                vowelCount += 1
            r += 1
            while r - l == k and l < len(s):
                mx = max(vowelCount, mx)
                if s[l] in vowels:
                    vowelCount -= 1
                l += 1
        return mx
