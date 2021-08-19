class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        N = len(A)
        prefix = [0]
        for _ in range(2):
            for x in A:
                prefix.append(prefix[-1] + x)
        res = A[0]
        deque = collections.deque([0])
        for j in range(1, len(prefix)):
            if deque[0] < j - N:
                deque.popleft()
            res = max(res, prefix[j] - prefix[deque[0]])
            while deque and prefix[j] <= prefix[deque[-1]]:
                deque.pop()
            deque.append(j)
        return res
