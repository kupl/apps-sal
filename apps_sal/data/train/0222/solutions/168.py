class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        set_a = set(A)
        seen = set()

        res = 0
        store = {}

        def find(x, y):
            if x + y in set_a:
                return 1 + find(y, x + y)
            else:
                return 0

        for i in range(n):
            for j in range(i + 1, n):
                if (A[i], A[j]) not in seen:
                    res = max(find(A[i], A[j]), res)

        if res == 0:
            return 0
        else:
            return res + 2
