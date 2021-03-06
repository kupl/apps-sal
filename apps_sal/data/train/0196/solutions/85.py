class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:

        def kadane(gen):
            size = len(gen)
            ans = cur = gen[0]
            for i in range(1, size):
                cur = max(gen[i], cur + gen[i])
                ans = max(ans, cur)
            return ans
        S = sum(A)
        ans1 = kadane(A)
        if len(A) > 1:
            ans2 = S + kadane([-A[i] for i in range(1, len(A))])
            ans3 = S + kadane([-A[i] for i in range(len(A) - 1)])
            return max(ans1, ans2, ans3)
        else:
            return ans1
