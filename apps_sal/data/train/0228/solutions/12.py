class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxVow, count = 0, 0
        for i, j in enumerate(s):
            if j in 'aeiou':
                count += 1
            if i >= k and s[i-k] in 'aeiou':
                count -= 1
            maxVow = max(maxVow, count)
        return maxVow
