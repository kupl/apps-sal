class Solution:

    def countTriplets(self, A: List[int]) -> int:
        n = len(A)
        n2 = n * n
        dp = {}
        ways = 0
        for i in range(n):
            for j in range(n):
                res = A[i] & A[j]
                dp[res] = dp.get(res, 0) + 1
        for i in range(n):
            for (tgt, ct) in dp.items():
                if A[i] & tgt == 0:
                    ways += ct
        return ways
