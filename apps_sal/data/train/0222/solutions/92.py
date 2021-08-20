class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        s = set(A)

        def helper(i, j):
            ans = 2
            while True:
                k = i + j
                if k in s and k <= 10 ** 9:
                    ans += 1
                    i = j
                    j = k
                else:
                    break
            return ans
        c = 0
        for i in reversed(list(range(n - 2))):
            for j in reversed(list(range(i + 1, n - 1))):
                c = max(c, helper(A[i], A[j]))
        return c if c > 2 else 0
