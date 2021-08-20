from collections import deque


class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        dq = deque()
        pre = [0]
        l = len(A)
        ans = l + 1
        for i in range(l):
            pre.append(pre[-1] + A[i])
        for i in range(l + 1):
            while dq and pre[dq[-1]] >= pre[i]:
                dq.pop()
            while dq and pre[dq[0]] + K <= pre[i]:
                ans = min(ans, i - dq.popleft())
            dq.append(i)
        return ans if ans < l + 1 else -1
