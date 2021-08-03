class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        seen = {}
        longest = 1
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                if (i, diff) not in seen:
                    seen[(i, diff)] = 1

                if (j, diff) not in seen:
                    seen[(j, diff)] = 1

                seen[(j, diff)] = max(seen[(j, diff)], seen[(i, diff)] + 1)

        return max([v for k, v in seen.items()])
