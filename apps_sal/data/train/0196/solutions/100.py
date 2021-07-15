class Solution:
    def maxSubarraySumCircular(self, A):
        # compute pre(k)
        # maximum continuous subarray that ends at end of A and starts after k
        pre = [0 for i in range(len(A))]

        pre_continuous = [0 for i in range(len(A))]
        pre_earlystop = [0 for i in range(len(A))]

        for i in range(len(A) - 2, -1, -1):
            pre_continuous[i] = pre_continuous[i + 1] + A[i + 1]
            pre_earlystop[i] = max(pre_earlystop[i + 1], pre_continuous[i])
            pre[i] = max(pre_continuous[i], pre_earlystop[i])

        # compute regular dp
        dp = [0 for i in range(len(A))]
        dp[0] = A[0]

        running_sum = A[0]
        best = dp[0] + pre[0]
        
        for i in range(1, len(A)):
            dp[i] = max(dp[i - 1] + A[i], A[i])

            best = max(best, dp[i], running_sum + pre[i])
            running_sum += A[i]

        return best
