class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        table = [collections.defaultdict(int) for _ in range(len(A))]
        ans = 0
        for i in range(len(A)):
            for j in range(i):
                if A[i] - A[j] in table[j]:
                    currLen = table[j][A[i] - A[j]] + 1
                else:
                    currLen = 2

                ans = max(ans, currLen)
                table[i][A[i] - A[j]] = max(table[i][A[i] - A[j]], currLen)
        return ans
