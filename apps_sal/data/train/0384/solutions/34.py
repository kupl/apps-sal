class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        l = len(A)
        p = [1]
        ans = 0
        for i in range(1, l):
            p.append(p[-1] * 2)
        for (i, j) in enumerate(A):
            ans += (p[i] - p[l - i - 1]) * j
        return ans % (10 ** 9 + 7)
