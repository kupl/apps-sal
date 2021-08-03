class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        d1 = {x: i for i, x in enumerate(A)}
        d2 = {}
        ans = 0
        for i in range(1, len(A)):
            for j in range(i):
                d2[(j, i)] = 2
                val = A[i] - A[j]
                if(val in d1 and d1[val] < j):
                    d2[(j, i)] = d2[(d1[val], j)] + 1
                    ans = max(ans, d2[(j, i)])

        if(ans >= 3):
            return ans
        return 0
