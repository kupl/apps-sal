class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        @lru_cache(None)
        def helper(s):
            if not s:
                return [[]]

            splits = []
            for i in range(1, len(s) + 1):
                word = s[:i]
                next_splits = helper(s[i:])
                for split in next_splits:
                    if word not in split:
                        splits.append(split + [word])

            return splits
        ret = helper(s)
        max_len = max([len(x) for x in ret])
        return max_len
