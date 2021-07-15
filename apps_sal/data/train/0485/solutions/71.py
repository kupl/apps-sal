class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        q = collections.deque()
        res = 0
        for i, num in enumerate(A):
            while len(q) > 0 and i - q[0] >= K:
                q.popleft()
            
            if len(q) % 2 == 1 and num == 1 or len(q) % 2 == 0 and num == 0:
                if i + K > len(A):
                    return -1
                q.append(i)
                res += 1
        return res
