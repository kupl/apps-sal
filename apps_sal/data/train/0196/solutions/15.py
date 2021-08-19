class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if A is None or not A:
            return 0
        N = len(A)
        A = A + A
        acc = [0]
        for d in A:
            acc.append(acc[-1] + d)
        ret = -sys.maxsize
        queue = deque([0])
        for j in range(1, 2 * N):
            while queue and queue[0] < j - N:
                queue.popleft()
            ret = max(ret, acc[j] - acc[queue[0]])
            while queue and acc[queue[-1]] >= acc[j]:
                queue.pop()
            queue.append(j)
        return ret
