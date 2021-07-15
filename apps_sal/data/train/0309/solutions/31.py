class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = dict()

        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if diff not in dp:
                    dp[diff] = {i: 2}
                else:
                    dic = dp[diff]
                    if j in dic:
                        dic[i] = dic[j] + 1
                    else:
                        dic[i] = 2

        return max(max(v1 for k1, v1 in list(v.items())) for k, v in list(dp.items()))

