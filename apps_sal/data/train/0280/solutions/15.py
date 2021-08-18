class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        dp = defaultdict(int)

        def pali(i, j):
            diff = 0
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    diff += 1
                dp[(i, j)] = diff
                i -= 1
                j += 1

        for i in range(len(s)):
            pali(i, i)
            pali(i, i + 1)

        @lru_cache(maxsize=None)
        def recurse(idx, numCuts):
            if numCuts > k:
                return float('inf')

            if idx == len(s):
                if numCuts == k:
                    return 0
                return float('inf')

            curMin = float('inf')
            for i in range(idx, len(s)):
                curMin = min(dp[(idx, i)] + recurse(i + 1, numCuts + 1), curMin)
            return curMin

        return recurse(0, 0)
