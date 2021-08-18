class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        pref = [0] + [*accumulate(A)]

        ans = math.inf
        q = deque()
        for i, s in enumerate(pref):
            while q and pref[q[-1]] >= s:
                q.pop()

            while q and s - pref[q[0]] >= K:
                ans = min(i - q[0], ans)
                q.popleft()

            q.append(i)

        return -1 if ans == math.inf else ans
