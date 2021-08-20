class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        d = [[0, 0]]
        (res, cur) = (float('inf'), 0)
        for (i, a) in enumerate(A):
            cur += a
            while d and cur - d[0][1] >= K:
                res = min(res, i - d.pop(0)[0] + 1)
            while d and cur <= d[-1][1]:
                d.pop()
            d.append([i + 1, cur])
        return res if res < float('inf') else -1
