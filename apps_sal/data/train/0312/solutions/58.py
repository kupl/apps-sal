class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:

        preSum = [0]
        for e in A:
            preSum.append(preSum[-1] + e)

        min_len = sys.maxsize

        q = collections.deque([])
        for i in range(len(preSum)):
            while q and preSum[q[-1]] > preSum[i]:
                q.pop()
            while q and preSum[i] - K >= preSum[q[0]]:
                min_len = min(min_len, i - q.popleft())

            q.append(i)

        return min_len if min_len != sys.maxsize else -1
