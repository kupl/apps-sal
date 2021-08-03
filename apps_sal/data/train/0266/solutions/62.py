class Solution:
    def numSplits(self, s: str) -> int:
        right = collections.Counter(s)
        left = collections.defaultdict(int)
        res = 0
        for i in range(len(s) - 1):
            c = s[i]
            right[c] -= 1
            if not right[c]:
                del right[c]
            left[c] += 1
            if len(left) == len(right):
                res += 1
        return res
