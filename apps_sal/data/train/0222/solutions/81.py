class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        def _helper(l1, l2, cache):
            if A[l1] + A[l2] in table:
                l1, l2 = l2, table[A[l1] + A[l2]]
                return _helper(l1, l2, cache + 1)
            else:
                return cache if cache >= 3 else 0
        ans = 0
        table = {v: i for i, v in enumerate(A)}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] + A[j] > A[-1]:
                    break
                ans = max(ans, _helper(i, j, 2))
        return ans
