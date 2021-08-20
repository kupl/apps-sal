class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        store = {}
        a_len = len(A)
        b_len = len(B)

        def f(a, b):
            if (a, b) in store:
                return store[a, b]
            if a == a_len or b == b_len:
                store[a, b] = 0
                return 0
            if A[a] == B[b]:
                store[a, b] = 1 + f(a + 1, b + 1)
            else:
                store[a, b] = max(f(a + 1, b), f(a, b + 1))
            return store[a, b]
        return f(0, 0)
