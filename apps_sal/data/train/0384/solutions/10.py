class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        if len(A) == 1:
            return 0
        if len(A) == 0:
            return 0
        (ans, prev, n, mod) = (A[1] - A[0], A[1] - A[0], len(A), 1000000000.0 + 7)
        (twoPow, temp) = ([1], 2)
        for i in range(1, n):
            twoPow.append(temp + twoPow[-1])
            temp = temp * 2 % mod
        for i in range(2, len(A)):
            diff = A[i] - A[i - 1]
            prev = (2 * (prev + diff * twoPow[i - 2] % mod) % mod + diff) % mod
            ans = (ans + prev) % mod
        return int(ans)
