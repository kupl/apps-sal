class Solution:

    def minKBitFlips(self, A: List[int], k: int) -> int:
        q = collections.deque()
        res = 0
        for i in range(len(A)):
            if len(q) % 2 == 0:
                if A[i] == 0:
                    res += 1
                    q.append(i + k - 1)
            elif A[i] == 1:
                res += 1
                q.append(i + k - 1)
            if q and q[0] == i:
                q.popleft()
            if q and q[-1] >= len(A):
                return -1
        return res
