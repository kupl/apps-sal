class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        dp = {}

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

        memo = {}

        def recurse(idx, numCuts):
            if numCuts == k and idx == len(s):
                return 0
            if numCuts == k or idx == len(s):
                return float('inf')

            if (idx, numCuts) in memo:
                return memo[(idx, numCuts)]
            curMin = float('inf')
            for j in range(idx, len(s)):
                curMin = min(dp[(idx, j)] + recurse(j + 1, numCuts + 1), curMin)
            memo[(idx, numCuts)] = curMin

            return curMin

        return recurse(0, 0)
