class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        biggest = max(A)

        def findLen(A: List[int]) -> int:
            seen = set()
            dp = defaultdict(lambda: defaultdict(lambda: 0))
            for a in A:
                for prev in seen:
                    gap = a - prev
                    newLen = 2 if dp[gap][prev] == 0 else 1 + dp[gap][prev]
                    dp[gap][a] = max(dp[gap][a], newLen)
                seen.add(a)
            return max([l for gaps in dp.values() for l in gaps.values()])
        return findLen(A)
