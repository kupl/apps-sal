class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        i = 0
        c = 0
        q = collections.deque()

        sign = 0
        while True:
            while i < len(A) and A[i] != sign:
                i += 1
                if q and i == q[0]:
                    q.popleft()
                    sign = 1 - sign

            if i == len(A):
                return c

            if i + K > len(A):
                return -1

            q.append(i + K)
            sign = 1 - sign

            c += 1
            i += 1
            if q and i == q[0]:
                q.popleft()
                sign = 1 - sign

        return c
