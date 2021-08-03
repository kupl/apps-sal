class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        maxCount = 0
        i = 0
        for j in range(len(s)):
            if s[j] in vowels:
                count += 1
            if j >= k and s[j - k] in vowels:
                count -= 1
            maxCount = max(maxCount, count)
        return maxCount
