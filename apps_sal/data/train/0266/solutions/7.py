from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        num_splits = 0
        left = Counter()
        right = Counter(s)

        for char in s:
            left.update(char)
            right.subtract(char)
            if right[char] == 0:
                del right[char]

            if len(left) == len(right):
                num_splits += 1

        return num_splits
