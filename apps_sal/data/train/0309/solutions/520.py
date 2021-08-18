class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)

        table = [defaultdict(int) for i in range(n)]
        out = 0
        curr = A[1] - A[0]
        full = True
        for i in range(2, n):
            if curr != A[i] - A[i - 1]:
                full = False
                break
        if full:
            return n

        for i in range(n):
            for j in range(0, i):
                diff = A[i] - A[j]
                if table[j][diff] == 0:
                    table[j][diff] = 1

                table[i][diff] = max(table[i][diff], table[j][diff] + 1)

                out = max(table[i][diff], out)

        return out
