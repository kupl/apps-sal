class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        L = len(A)
        
        # reduced_dp[i] store the value of dp[i][K]
        # the `k` in dp[i] is implicity indicated by the loop
        reduced_dp = [0 for _ in range(L)]        
        prefix_sum = [0 for _ in range(L + 1)]
        for i in range(1, L + 1):
            prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]
            reduced_dp[i - 1] = prefix_sum[i] / i;

        # for i in reduced_dp:
        #     print(i)

        for k in range(2, K + 1):
            for i in reversed(range(1, L)):
                if k <= i + 1:
                    for j in range(-1, i):
                        ave = (prefix_sum[i + 1] - prefix_sum[j + 1]) / (i - j)
                        if j == -1:
                            tmp = 0
                        else:
                            tmp = reduced_dp[j]
                        if ave + tmp > reduced_dp[i]:
                            reduced_dp[i] = ave + tmp
                            
        # for i in reduced_dp:
        #     print(i)
        # print('done')
        return reduced_dp[-1]
