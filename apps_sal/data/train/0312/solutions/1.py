class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        queue = collections.deque([(0, -1)])
        prefix_sum = 0
        res = float('inf')
        for i in range(len(A)):
            prefix_sum += A[i]
            while queue and queue[-1][0] > prefix_sum:
                queue.pop()

            while queue and prefix_sum - queue[0][0] >= K:
                res = min(res, i - queue[0][1])
                queue.popleft()

            queue.append((prefix_sum, i))
        return res if res != float('inf') else -1
