from collections import deque


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        arr = A + A
        arr = arr[:-1]

        prefix = [0] * len(arr)
        prefix[0] = arr[0]
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] + arr[i]

        prefix.insert(0, 0)
        # monotonic increasing array
        dq = deque([0])
        res = -float('inf')
        for i in range(1, len(prefix)):

            while dq and i - dq[0] > len(A):
                dq.popleft()
            if dq:
                res = max(res, prefix[i] - prefix[dq[0]])

            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            dq.append(i)

        return res
