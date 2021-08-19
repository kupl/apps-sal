class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        ret = 0
        cnt = 0
        for i in range(k):
            if self.vowel(s[i]):
                cnt += 1
        ret = max(ret, cnt)
        for i in range(k, len(s)):
            if self.vowel(s[i]):
                cnt += 1
            if self.vowel(s[i - k]):
                cnt -= 1
            ret = max(ret, cnt)
        return ret

    def vowel(self, char):
        return char in ['a', 'e', 'i', 'o', 'u']
