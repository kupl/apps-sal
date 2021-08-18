class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        A *= 2
        ans = [A[0]] + [0] * (len(A) - 1)
        q = collections.deque([(0, A[0])])
        cur = A[0]
        for i, a in enumerate(A[1:], 1):
            while q and i - q[0][0] > n:
                q.popleft()
            cur += a
            ans[i] = cur - q[0][1]
            while q and q[-1][1] >= cur:
                q.pop()
            q.append((i, cur))
        return max(ans)
