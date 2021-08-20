class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        if n == 0:
            return -1
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + A[i - 1]
        queue = collections.deque()
        queue.append((0, 0))
        res = n + 1
        for i in range(1, n + 1):
            while queue:
                (qi, qe) = queue[0]
                if qe + K <= dp[i]:
                    res = min(res, i - qi)
                    queue.popleft()
                else:
                    break
            while queue:
                (_, qe) = queue[-1]
                if qe >= dp[i]:
                    queue.pop()
                else:
                    break
            queue.append((i, dp[i]))
        if res == n + 1:
            return -1
        else:
            return res
