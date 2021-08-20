class Solution:

    def count_chars(self, s):
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        return count

    def dict_decr(self, d, c):
        if c in d:
            d[c] -= 1
        if d[c] <= 0:
            del d[c]

    def numSplits(self, s: str) -> int:
        (left, right) = (s[0], s[1:])
        left_chars = set([left])
        right_chars = self.count_chars(right)
        num_splits = 0
        while right:
            if len(left_chars) == len(right_chars.keys()):
                num_splits += 1
            c = right[0]
            self.dict_decr(right_chars, c)
            left_chars.add(c)
            left += c
            right = right[1:]
        return num_splits
