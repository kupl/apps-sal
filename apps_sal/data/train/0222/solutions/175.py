class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        mem = collections.defaultdict(Counter)
        ans = 0
        for i in range(0, n):
            for j in range(i - 1, -1, -1):
                dij = A[i] - A[j]
                djk = A[j] - dij
                if djk in mem[A[j]]:
                    mem[A[i]][dij] = 1 + mem[A[j]][djk]
                else:
                    mem[A[i]][dij] = 2
                ans = max(ans, mem[A[i]][dij])
        if ans < 3:
            return 0
        return ans
