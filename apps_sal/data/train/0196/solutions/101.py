from collections import deque
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        B = A + A
        N = len(A)
        queue = deque([0])
        pre_sum = [0]
        for i in range(len(B)):
            pre_sum.append(pre_sum[-1] + B[i])
        ans = A[0]
        for j in range(1, len(pre_sum)):
            if j - queue[0] > N:
                queue.popleft()
            ans = max(ans, pre_sum[j] - pre_sum[queue[0]])
            while queue and pre_sum[queue[-1]] >= pre_sum[j]:
                queue.pop()
            queue.append(j)
        return ans 

