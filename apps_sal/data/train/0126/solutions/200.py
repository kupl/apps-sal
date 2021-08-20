from collections import Counter


class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt = Counter()
        word_cnt = Counter()
        cur_hash = 0
        left = 0
        res = 0
        i = 0
        while i < len(s):
            if i - left + 1 > minSize:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
            cnt[s[i]] += 1
            if len(cnt) <= maxLetters and i - left + 1 == minSize:
                word_cnt[s[left:i + 1]] += 1
                res = max(res, word_cnt[s[left:i + 1]])
            i += 1
        return res
