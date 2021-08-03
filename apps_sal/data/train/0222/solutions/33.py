class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        index = {x: i for i, x in enumerate(A)}
        longest = [[2 for i in range(len(A))] for j in range(len(A))]

        ans = 0
        for k, z in enumerate(A):
            for j in range(k):
                i = index.get(z - A[j], None)
                if i is not None and i < j:
                    longest[j][k] = longest[i][j] + 1
                    ans = max(ans, longest[j][k])
        return ans if ans >= 3 else 0
