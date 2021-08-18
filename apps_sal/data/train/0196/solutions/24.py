class Solution:
    def maxSubarraySumCircular(self, A):
        def kadane(gen):
            ans = cur = float('-inf')
            for x in gen:
                cur = max(cur, 0) + x
                ans = max(ans, cur)
            return ans

        S = sum(A)
        ans1 = kadane(iter(A))
        ans2 = S + kadane(-A[i] for i in range(1, len(A)))
        ans3 = S + kadane(-A[i] for i in range(len(A) - 1))

        return max(ans1, ans2, ans3)
