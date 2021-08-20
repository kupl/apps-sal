from collections import deque


class Solution:

    def minKBitFlips(self, A: List[int], K: int) -> int:
        s = deque()
        count = 0
        for i in range(len(A)):
            while s and s[0] + K <= i:
                s.popleft()
            flip = len(s) % 2 == 1
            ok = flip ^ A[i]
            if not ok:
                if i + K > len(A):
                    return -1
                s.append(i)
                count += 1
        return count
