class Solution:

    def maxRepOpt1(self, text: str) -> int:
        text_cnt = collections.Counter(text)
        d = collections.Counter()
        (l, r) = (0, 0)
        maxcnt = 0
        res = 0
        N = len(text)
        for (r, ch) in enumerate(text):
            d[ch] += 1
            maxcnt = max(maxcnt, d[ch])
            while r - l + 1 > maxcnt + 1:
                d[text[l]] -= 1
                maxcnt = max(d.values())
                l += 1
            res = max(res, min(r - l + 1, text_cnt[ch]))
        return res
