class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        from itertools import combinations
        for k in reversed(list(range(len(s) + 1))):
            for comb in combinations(list(range(1, len(s))), k):
                split_idxs = [0, *comb, len(s)]
                splits = []
                for prev, next in zip(split_idxs, split_idxs[1:]):
                    splits.append(s[prev:next])
                if len(set(splits)) == len(splits):
                    return len(splits)
        return 0
