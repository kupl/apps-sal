class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        stored = [{} for i in range(len(A))]
        best = 0
        for (index, value) in enumerate(A):
            if index == 0:
                continue
            for compare in range(index):
                difference = value - A[compare]
                stored[index][difference] = 1 + stored[compare].get(difference, 1)
                best = max(best, stored[index][difference])
        return best
