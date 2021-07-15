class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        flips = 0
        q = deque()
        for i, x in enumerate(A):
            if q and q[0] == i:
                q.popleft()
            if len(q) & 1:
                x ^= 1
            if x == 0:
                flips += 1
                q.append(i + K)
                if i + K > len(A):
                    return -1
        return flips
