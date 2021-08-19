class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        cur = 0
        for (j, c) in enumerate(s):
            cur += c in 'aeiou'
            if j >= k:
                cur -= s[j - k] in 'aeiou'
            ans = max(ans, cur)
        return max(ans, cur)
