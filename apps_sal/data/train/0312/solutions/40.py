class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        psum = 0
        total = 0
        dq = deque([(0, -1)])
        res = float('inf')
        for i, a in enumerate(A):
            psum += a
            while dq and dq[-1][0] > psum:
                dq.pop()

            while dq and psum - dq[0][0] >= K:
                res = min(res, i - dq.popleft()[1])
            dq.append((psum, i))
        return res if res != float('inf') else -1
