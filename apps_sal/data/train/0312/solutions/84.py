class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        queue = collections.deque()
        Sum, res = 0, float('inf')
        queue.append((0, -1))
        for i, v in enumerate(A):
            Sum += v

            while queue and Sum - queue[0][0] >= K:
                res = min(res, i - queue.popleft()[1])
            while queue and Sum <= queue[-1][0]:
                queue.pop()
            queue.append((Sum, i))

        return res if res < float('inf') else -1
