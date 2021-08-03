from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt = defaultdict(int)
        freq = defaultdict(int)
        res, left = 0, 0
        for i in range(len(s)):
            cnt[s[i]] = cnt.get(s[i], 0) + 1
            while len(cnt) > maxLetters or i - left + 1 > minSize:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
            if (i - left + 1 <= maxSize and i - left + 1 >= minSize):
                sub = s[left: i + 1]
                freq[sub] = freq.get(sub, 0) + 1
        return max(freq.values()) if freq else 0
