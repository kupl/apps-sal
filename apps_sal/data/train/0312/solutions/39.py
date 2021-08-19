from collections import deque


class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        q = deque([(0, 0)])
        (presum, ans) = (0, float('inf'))
        for (idx, n) in enumerate(A):
            presum += n
            while q and presum - q[0][1] >= K:
                ans = min(ans, idx + 1 - q.popleft()[0])
            while q and q[-1][1] >= presum:
                q.pop()
            q.append((idx + 1, presum))
        return ans if ans < float('inf') else -1
