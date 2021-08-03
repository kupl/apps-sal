class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        L = len(A)
        dp = [
            [0 for _ in range(K + 1)] for _out in range(L)
        ]

        dp[0][1] = A[0]
        for i in range(1, L):
            dp[i][1] = (dp[i - 1][1] * i + A[i]) / (i + 1)
        # for i in dp:
        #     print(i)

        for i in range(1, L):
            for k in range(2, K + 1):
                if k > i + 1:
                    dp[i][k] = dp[i][k - 1]
                else:
                    for j in range(-1, i):
                        subarr = A[j + 1: i + 1]
                        # print(j, i, subarr)
                        ave = sum(subarr) / len(subarr)
                        if j == -1:
                            tmp = 0
                        else:
                            tmp = dp[j][k - 1]
                        # print(ave, tmp)
                        if ave + tmp > dp[i][k]:
                            dp[i][k] = ave + tmp
        # for i in dp:
        #     print(i)
        # print('done')
        return dp[-1][-1]
