class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        mem = {}
        for (idx, x) in enumerate(A):
            for i2 in range(idx):
                v2 = A[i2]
                if v2 < x:
                    mem[v2, x] = 1 + mem.get((x - v2, v2), 1)
        res = max(mem.values())
        return 0 if res == 2 else res
