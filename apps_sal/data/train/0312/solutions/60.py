class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        d = collections.deque([[0, 0]])
        res, cur = len(A) + 1, 0
        for i, a in enumerate(A):
            cur += a
            while d and cur - d[0][1] >= K:
                res = min(res, i + 1 - d.popleft()[0])
            while d and cur <= d[-1][1]:  # new i make the further subarray length shorter and sum bigger
                d.pop()
            d.append([i + 1, cur])
        return res if res < len(A) + 1 else -1
