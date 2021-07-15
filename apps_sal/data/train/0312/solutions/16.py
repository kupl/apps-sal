class Solution:
    def shortestSubarray(self, A: List[int], k: int) -> int:
        # d = collections.deque([[0, 0]])
        # res, cur = float('inf'), 0
        # for i, a in enumerate(A):
        #     cur += a
        #     while d and cur - d[0][1] >= K:
        #         res = min(res, i + 1 - d.popleft()[0])
        #     while d and cur <= d[-1][1]:
        #         d.pop()
        #     d.append([i + 1, cur])
        # return res if res < float('inf') else -1
        
        d = collections.deque([[0,0]])
        cur = 0
        res = float('inf')
        
        for i, a in enumerate(A):
            cur += a
            while d and cur - d[0][1] >= k:
                l = d.popleft()[0]
                res = min(res, i - (l-1))
            while d and cur <= d[-1][1]:
                d.pop()
            d.append([i+1, cur])
        return res if res < float('inf') else -1

