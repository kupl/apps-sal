import functools


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        @functools.lru_cache(None)
        def dp(i):
            res = [{s[:i + 1]}]
            for j in range(0, i):
                for sets in dp(j):
                    if s[j + 1:i + 1] not in sets:
                        res.append(sets | {s[j + 1:i + 1]})
            return res
        return max([len(set_) for set_ in dp(len(s) - 1)])
