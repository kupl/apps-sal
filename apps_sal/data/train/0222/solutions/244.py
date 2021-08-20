class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        index = {A[i]: i for i in range(len(A))}
        longest = {}
        ans = 0
        length = len(A)
        for i in range(length):
            for j in range(i):
                x = A[i] - A[j]
                m = index.get(x)
                if m is not None and m < j:
                    longest[j, i] = longest.get((m, j)) + 1 if longest.get((m, j)) is not None else 3
                    ans = max(ans, longest[j, i])
                else:
                    continue
        return ans if ans >= 3 else 0
