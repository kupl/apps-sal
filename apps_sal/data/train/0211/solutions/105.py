from itertools import combinations


class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        for num_splits in reversed(range(1, len(s))):
            num_strings = num_splits + 1
            for split_indices in combinations(range(1, len(s)), num_splits):
                indices = [0] + list(split_indices) + [len(s)]
                split_strs = set()
                for (start, end) in zip(indices[:-1], indices[1:]):
                    split_strs.add(s[start:end])
                if len(split_strs) == num_strings:
                    return num_strings
        return 1
