class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        dq = deque()
        res = 0
        for i in range(len(A)):
            if A[i] == len(dq) % 2:
                res += 1
                dq.append(i+K-1)
                
            if dq and dq[0] <= i:
                dq.popleft()
                
        return res if not dq else -1
