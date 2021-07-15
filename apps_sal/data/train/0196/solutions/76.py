class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        ans1 = cur = 0
        for x in A:
            cur = x + max(cur, 0)
            ans1 = max(ans1, cur)
        
        ans2 = cur = 0
        for i in range(1, len(A)):
            cur = A[i] + min(cur, 0)
            ans2 = min(ans2, cur)
        ans2 = sum(A) - ans2
        
        ans3 = cur = 0
        for i in range(len(A)-1):
            cur = A[i] + min(cur, 0)
            ans3 = min(ans3, cur)
        ans3 = sum(A) - ans3
        
        ans = max(ans1, ans2, ans3)
        return ans if ans != 0 else max(A)

