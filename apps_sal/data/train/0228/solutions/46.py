class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        currMax = 0
        curr = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for i, c in enumerate(s):
            if c in vowels:
                curr += 1
            if i >= k and s[i - k] in vowels:
                curr -= 1
            currMax = max(curr, currMax)
            if currMax == k:
                break
        return currMax
