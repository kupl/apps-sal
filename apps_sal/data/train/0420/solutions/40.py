class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        seen = {(0, 0, 0, 0, 0): -1}
        vowel = 'aeiou'
        count = [0] * 5
        ans = 0
        for i in range(len(s)):
            idx = vowel.find(s[i])
            if idx >= 0:
                count[idx] += 1
            state = tuple([count[i] % 2 for i in range(5)])
            if state in seen:
                ans = max(ans, i - seen[state])
            else:
                seen[state] = i
        return ans
