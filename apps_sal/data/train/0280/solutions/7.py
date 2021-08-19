class Solution:
    def palindromePartition(self, s: str, key: int) -> int:

        @lru_cache(None)
        def repair(string: s) -> int:
            return sum([1 if string[i] != string[-1 - i] else 0 for i in range(len(string) // 2)])

        @lru_cache(None)
        def pp(start: int, end: int, k: int) -> int:
            # print(\"s:\", s, k)
            if k == len(s):
                return 0
            elif k == 1:
                return repair(s[start:end])
            changes = end - start - k
            for i in range(k - 1, end - start):
                changes = min(pp(start, i, k - 1) + repair(s[i:end]), changes)
            return changes

        return pp(0, len(s), key)
