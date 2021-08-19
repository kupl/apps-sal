from collections import Counter


class Solution:

    def numSplits(self, s):
        res = 0
        left = {}
        right = Counter(s)
        for i in range(len(s)):
            left[s[i]] = left.get(s[i], 0) + 1
            right[s[i]] -= 1
            if right[s[i]] == 0:
                del right[s[i]]
            if len(left) == len(right):
                res += 1
        return res
