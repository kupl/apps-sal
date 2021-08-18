class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        N, res = len(s), 0

        for i in range(2 ** (N - 1)):
            start, seen = 0, set()
            for j in range(N):
                if (i + (1 << N - 1)) & (1 << j):
                    seen.add(s[start: j + 1])
                    start = j + 1

            res = max(res, len(seen))

        return res
