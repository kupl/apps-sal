class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        q = collections.deque()
        res = 0
        for i in range(len(A)):
            if A[i] == len(q) % 2:
                q.append(i)
                res += 1
            
            if q and q[0] <= i - K + 1:
                q.popleft()
        return res if len(q) == 0 else -1
