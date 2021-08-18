class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        res = n + 1
        Sum = 0
        dq = collections.deque([(-1, 0)])

        for i, val in enumerate(A):
            Sum += val
            if val > 0:
                while dq and Sum - dq[0][1] >= K:
                    res = min(res, i - dq.popleft()[0])
            else:
                while dq and Sum < dq[-1][1]:
                    dq.pop()
            dq.append((i, Sum))

        if res <= n:
            return res
        else:
            return -1
