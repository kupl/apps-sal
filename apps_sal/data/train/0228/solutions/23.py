class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        total = res = 0
        for i in range(len(s)):
            if s[i] in 'aeiou':
                total += 1
            if i >= k - 1:
                res = max(res, total)
                if s[i - k + 1] in 'aeiou':
                    total -= 1
        return res
