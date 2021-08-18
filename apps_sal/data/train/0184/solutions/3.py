import itertools
import collections


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        import collections
        counter = collections.Counter(text)
        cnt = collections.defaultdict(int)
        start = res = max_cnt = 0
        for end, char in enumerate(text):
            cnt[char] += 1
            max_cnt = max(max_cnt, cnt[char])
            while end - start + 1 > max_cnt + 1:
                cnt[text[start]] -= 1
                max_cnt = max(cnt.values())
                start += 1
            res = max(res, min(end - start + 1, counter[char]))
        return res
