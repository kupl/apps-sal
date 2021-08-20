class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        """
            2:35
            # prefix sum  O(n)
            # for each L subarray:  O(n)
                check all M subarrays in its left or right, O(n)

            # O(n^2)
        """
        N = len(A)
        prefix = [0] * (N + 1)
        for i in range(1, N + 1):
            prefix[i] = prefix[i - 1] + A[i - 1]
        res = 0
        for Li in range(N - L + 1):
            Lj = Li + L
            sumL = prefix[Lj] - prefix[Li]
            sumM = 0
            for Mi in range(Lj, N - M + 1):
                Mj = Mi + M
                sumM = max(sumM, prefix[Mj] - prefix[Mi])
            for Mi in range(0, Li - M + 1):
                Mj = Mi + M
                sumM = max(sumM, prefix[Mj] - prefix[Mi])
            res = max(res, sumL + sumM)
        return res
