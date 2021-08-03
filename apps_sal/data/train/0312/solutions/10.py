class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        L = len(A)
        min_length = L + 1
        queue = collections.deque([(0, -1)])
        cursum = 0
        for i in range(L):
            cursum += A[i]
            while queue and cursum - queue[0][0] >= K:
                prevSum, prevIdx = queue.popleft()
                min_length = min(min_length, i - prevIdx)
            while queue and queue[-1][0] >= cursum:
                queue.pop()
            queue.append((cursum, i))

        return min_length if min_length <= L else -1
