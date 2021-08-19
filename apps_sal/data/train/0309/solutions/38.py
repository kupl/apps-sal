class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        answer = 2
        L = len(A)
        table = [dict() for _ in range(L)]
        for i in range(1, L):
            for j in range(0, i):
                diff = A[i] - A[j]
                if not diff in table[j]:
                    table[i][diff] = 2
                else:
                    table[i][diff] = table[j][diff] + 1
                    answer = max(answer, table[i][diff])
        return answer
