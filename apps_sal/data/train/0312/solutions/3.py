class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        B = [0]
        for a in A:
            B.append(B[-1] + a)
        print(B)
        dq = collections.deque()
        res = float('inf')
        for (i, n) in enumerate(B):
            while dq and B[dq[-1]] >= n:
                dq.pop()
            while dq and n - B[dq[0]] >= K:
                res = min(res, i - dq[0])
                dq.popleft()
            dq.append(i)
        return -1 if res == float('inf') else res
