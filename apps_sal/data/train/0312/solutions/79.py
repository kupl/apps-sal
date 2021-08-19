from collections import deque


class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        prefix_sum = [0 for _ in range(n + 1)]
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]
        dq = deque()
        ans = n + 1
        for i in range(len(prefix_sum)):
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= K:
                ans = min(ans, i - dq[0])
                dq.popleft()
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()
            dq.append(i)
        return -1 if ans == n + 1 else ans
