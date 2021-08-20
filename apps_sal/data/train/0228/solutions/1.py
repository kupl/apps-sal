class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])
        res = 0
        cnt = 0
        for i in range(k):
            if s[i] in vowels:
                cnt += 1
        res = max(res, cnt)
        for i in range(k, len(s)):
            if s[i] in vowels:
                cnt += 1
            if s[i - k] in vowels:
                cnt -= 1
            res = max(res, cnt)
        return res
