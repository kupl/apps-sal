class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        seen = set()
        for i in range(len(A)):
            for j in range(i, len(A)):
                seen.add(A[j] - A[i])
        ans = 0
        for j in seen:
            d = defaultdict(int)
            for i in A:
                d[i] = d[i - j] + 1
                ans = max(ans, d[i])
        return ans
