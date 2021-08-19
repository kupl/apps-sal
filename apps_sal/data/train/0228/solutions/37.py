class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        if len(s) < k:
            k = len(s)
        cnt = 0
        for i in range(k):
            if s[i] in ('a', 'e', 'i', 'o', 'u'):
                cnt += 1
        max_cnt = cnt
        for i in range(k, len(s)):
            if s[i] in ('a', 'e', 'i', 'o', 'u'):
                cnt += 1
            if s[i - k] in ('a', 'e', 'i', 'o', 'u'):
                cnt -= 1
            max_cnt = max(max_cnt, cnt)
        return max_cnt
