from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = defaultdict(lambda: 0)
        for word in sorted(words, key=len):
            dp[''.join(sorted(word))] = max(dp[''.join(sorted(word[:idx] + word[idx + 1:]))] for idx in range(len(word))) + 1
        return max(dp.values())

