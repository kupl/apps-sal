from collections import Counter


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # greed algorithm: only focus the substring with length == minSize
        # also, apply continuous hashing function
        power = 26 ** (minSize - 1)
        cnt = Counter()
        word_cnt = Counter()
        cur_hash = 0
        left = 0
        res = 0
        right = 0
        while right < minSize:
            cnt[s[right]] += 1
            cur_hash = cur_hash * 26 + (ord(s[right]) - ord('a') + 1)
            right += 1

        word_cnt[cur_hash] = 1
        while right < len(s):
            if right - left + 1 > minSize:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                cur_hash = cur_hash - power * (ord(s[left]) - ord('a') + 1)
                left += 1

            cnt[s[right]] += 1
            cur_hash = cur_hash * 26 + (ord(s[right]) - ord('a') + 1)

            if len(cnt) <= maxLetters and right - left + 1 == minSize:
                word_cnt[cur_hash] += 1
                res = max(res, word_cnt[cur_hash])

            right += 1

        return res
# \"aababcaab\"
# 2
# 3
# 4
# \"aaaa\"
# 1
# 3
# 3
# \"aabcabcab\"
# 2
# 2
# 3
# \"abcde\"
# 2
# 3
# 3
