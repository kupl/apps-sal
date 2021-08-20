class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        queue = collections.deque([[0, 0]])
        res = float('inf')
        curr = 0
        for (i, a) in enumerate(A):
            curr += a
            while queue and curr - queue[0][1] >= K:
                tmp = queue.popleft()
                res = min(res, i - tmp[0] + 1)
            while queue and curr < queue[-1][1]:
                queue.pop()
            queue.append([i + 1, curr])
        return res if res != float('inf') else -1
