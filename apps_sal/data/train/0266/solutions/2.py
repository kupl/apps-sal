from collections import Counter


class Solution:

    def numSplits(self, s: str) -> int:
        right = Counter(s)
        left = set()
        res = 0
        for i in range(len(s) - 1):
            left.add(s[i])
            right[s[i]] -= 1
            res += len(left) == sum((i > 0 for i in right.values()))
        return res
