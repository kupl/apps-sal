class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        res = 0
        q = deque()
        for i in range(len(A)):
            if len(q) % 2 != 0:
                if A[i] == 1:
                    res += 1
                    q.append(i + K - 1)
            else:
                if A[i] == 0:
                    res += 1
                    q.append(i + K - 1)
            if q and q[0] == i:
                q.popleft()
            if q and q[-1] >= len(A):
                return -1
        return res

