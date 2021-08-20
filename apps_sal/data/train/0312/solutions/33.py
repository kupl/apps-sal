class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        pref = [0] + list(itertools.accumulate(A))
        q = deque()
        ans = math.inf
        for (i, n) in enumerate(pref):
            while q and pref[q[-1]] > n:
                q.pop()
            while q and n - pref[q[0]] >= K:
                ans = min(ans, i - q.popleft())
            q.append(i)
        return -1 if ans == math.inf else ans
