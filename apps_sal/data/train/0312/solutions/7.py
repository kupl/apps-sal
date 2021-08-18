class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        preSum = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + A[i - 1]
        deque = []
        i = 0
        ans = n + 1
        while i <= n:
            while deque and preSum[i] - preSum[deque[0]] >= K:
                ans = min(ans, i - deque[0])
                print(ans)
                deque.pop(0)
            while deque and preSum[deque[-1]] >= preSum[i]:
                deque.pop()
            deque.append(i)
            i += 1
        return ans if ans < n + 1 else -1
