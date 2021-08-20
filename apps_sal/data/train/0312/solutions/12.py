class Solution:

    def shortestSubarray(self, A: List[int], k: int) -> int:
        prefixSum = [0]
        for i in range(len(A)):
            prefixSum.append(prefixSum[-1] + A[i])
        q = collections.deque()
        out = sys.maxsize
        for i in range(len(prefixSum)):
            while q and prefixSum[i] - prefixSum[q[0]] >= k:
                out = min(out, i - q.popleft())
            while q and prefixSum[i] <= prefixSum[q[-1]]:
                q.pop()
            q.append(i)
        return out if out != sys.maxsize else -1
