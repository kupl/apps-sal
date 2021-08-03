class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        presum = [0]
        for a in A:
            presum.append(presum[-1] + a)

        def helper(A, l1, l2):
            res = 0
            N = len(A)
            for i in range(N - l1 + 1 - l2):
                for j in range(i + l1, N - l2 + 1):
                    s1 = presum[i + l1 - 1 + 1] - presum[i]
                    s2 = presum[j + l2 - 1 + 1] - presum[j]
                    res = max(res, s1 + s2)

            return res

        r1 = helper(A, L, M)
        r2 = helper(A, M, L)
        return max(r1, r2)
