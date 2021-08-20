class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        ans = len(A) + 1
        S = deque()
        S.append([0, -1])
        for (i, x) in enumerate(A):
            cur = S[-1][0] + x
            while S and S[-1][0] >= cur:
                S.pop()
            S.append([cur, i])
            while S[-1][0] >= S[0][0] + K:
                ans = min(ans, S[-1][1] - S.popleft()[1])
        return ans if ans <= len(A) else -1
