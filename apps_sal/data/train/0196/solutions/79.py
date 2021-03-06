class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        A *= 2
        ans = [0] * len(A)
        q = collections.deque()
        cur = 0
        for (i, a) in enumerate(A):
            while q and i - q[0][0] > n:
                q.popleft()
            cur += a
            ans[i] = cur - q[0][1] if q else cur
            while q and q[-1][1] >= cur:
                q.pop()
            q.append((i, cur))
        return max(ans)
