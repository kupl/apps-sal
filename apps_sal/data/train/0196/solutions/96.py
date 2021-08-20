class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        l = len(A)
        A = A + A
        q = collections.deque([(0, -1)])
        cur = 0
        ret = float('-inf')
        for (i, num) in enumerate(A):
            cur += num
            ret = max(ret, cur - q[0][0])
            if q[0][1] + l == i:
                q.popleft()
            while len(q) > 0 and q[-1][0] > cur:
                q.pop()
            q.append((cur, i))
        return ret
