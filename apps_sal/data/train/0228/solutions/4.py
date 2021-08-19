class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        cnt = 0
        for i in range(k):
            if s[i] in vowel:
                cnt += 1
        if cnt == k:
            return k
        i = 0
        res = cnt
        for j in range(k, len(s)):
            if s[i] in vowel:
                cnt -= 1
            if s[j] in vowel:
                cnt += 1
            i += 1
            if cnt == k:
                return k
            res = max(res, cnt)
        return res
