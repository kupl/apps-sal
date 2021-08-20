from collections import deque


class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        if max(A) >= K:
            return 1
        if K <= 0:
            return -1
        psum = [0]
        for a in A:
            psum.append(psum[-1] + a)
        window = deque([(0, 0)])
        res = float('inf')
        for right in range(len(A)):
            while window and psum[right + 1] <= window[-1][1]:
                window.pop()
            window.append((right + 1, psum[right + 1]))
            while window and window[-1][1] - window[0][1] >= K:
                res = min(res, window[-1][0] - window[0][0])
                window.popleft()
        return res if res != float('inf') else -1
