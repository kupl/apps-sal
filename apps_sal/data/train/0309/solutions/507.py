class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        hm = {A[0]: 0}
        for i in range(1, len(A)):
            if A[i] not in hm:
                hm[A[i]] = i
            for j in range(i):
                diff = A[i] - A[j]
                # print(i, j, diff, dp, hm)
                if (A[j] - diff) in hm:
                    dp[(i, diff)] = max(dp.get((i, diff), 2), dp.get((j, diff), 1) + 1)
                else:
                    dp[(i, diff)] = max(dp.get((i, diff), 2), 2)

        # print(dp)
        return max(dp.values())
