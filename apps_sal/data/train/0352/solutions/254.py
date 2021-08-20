from collections import defaultdict


class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        ends_at = defaultdict(int)
        words = sorted(words, key=lambda x: len(x))
        ans = 0
        for w in words:
            ends_at[w] = 1
            for (i, ch) in enumerate(w):
                prev = w[:i] + w[i + 1:]
                if prev in words:
                    ends_at[w] = max(ends_at[w], ends_at[prev] + 1)
            ans = max(ans, ends_at[w])
        return ans
