class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        if max(A) >= K:
            return 1
        n = len(A)
        prefix = [0] + list(itertools.accumulate(A))
        res = n + 1
        dq = deque()
        for (y, py) in enumerate(prefix):
            while dq and prefix[dq[-1]] > py:
                dq.pop()
            while dq and py - prefix[dq[0]] >= K:
                res = min(res, y - dq.popleft())
            dq.append(y)
        return res if res <= n else -1
