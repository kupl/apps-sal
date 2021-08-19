class Solution:

    def countTriplets(self, A: List[int]) -> int:
        from collections import defaultdict
        dic = defaultdict(int)
        n = len(A)
        dp = defaultdict(int)
        for i in range(n):
            for j in range(n):
                dic[i, j] = A[i] & A[j]
                dp[A[i] & A[j]] += 1
        ans = 0
        for i in range(n):
            for x in dp:
                if x & A[i] == 0:
                    ans += dp[x]
        return ans
