class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def kadane(aa):
            ans = cur = float('-inf')
            for v in aa:
                cur = max(cur, 0) + v
                ans = max(ans, cur)
            return ans
        S = sum(A)
        ans1 = kadane(A)
        ans2 = S + kadane(-A[i] for i in range(1, len(A)))
        ans3 = S + kadane(-A[i] for i in range(len(A) - 1))
        return max(ans1, ans2, ans3)
