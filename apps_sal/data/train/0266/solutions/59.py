class Solution:

    def numSplits(self, s: str) -> int:
        if len(s) < 2:
            return 0
        c = 0
        (left, right) = (defaultdict(int), defaultdict(int))
        left[s[0]] = 1
        for i in range(1, len(s)):
            right[s[i]] += 1
        if len(right) == 1:
            c += 1
        for i in range(1, len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
            left[s[i]] += 1
            if len(left) == len(right):
                c += 1
        return c
