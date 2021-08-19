class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        dp = [0]
        for _ in range(2):
            for num in A:
                dp.append(dp[-1] + num)

        res = A[0]
        deque = collections.deque([0])  # i's, increasing by P[i]
        for j in range(1, len(dp)):
            # If the smallest i is too small, remove it.
            if deque[0] < j - len(A):
                deque.popleft()

            # The optimal i is deque[0], for cand. answer P[j] - P[i].
            res = max(res, dp[j] - dp[deque[0]])

            # Remove any i1's with P[i2] <= P[i1].
            while deque and dp[j] <= dp[deque[-1]]:
                deque.pop()

            deque.append(j)
        return res
        '''
        As before, sum(nums[i:i+k]) = dp[i+k]-dp[i]
        now, sum[i+k:i] = dp[len(A)-(i+k)]+dp[i]
        '''
        cur_max = -float('inf')
        dp = [0]
        for num in A:
            dp.append(dp[-1] + num)

        for i in range(len(A)):
            for j in range(i + 1, i + len(A) + 1):
                if j <= len(A):
                    cur_max = max(cur_max, dp[j] - dp[i])
                else:
                    cur_max = max(cur_max, dp[len(A)] - dp[i] + dp[j % len(A)])
        return cur_max
