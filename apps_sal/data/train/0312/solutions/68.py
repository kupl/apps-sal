class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        p, n = [0], len(A)
        for i in range(n):
            p.append(p[-1] + A[i])
        i, ret = 0, float('inf')
        q = collections.deque()
        while i < n + 1:
            while q and p[q[-1]] > p[i]:
                q.pop()
            q.append(i)
            while q and p[q[-1]] - p[q[0]] >= K:
                ind = q.popleft()
                ret = min(ret, q[-1] - ind)
            i += 1
        return ret if ret != float('inf') else -1
