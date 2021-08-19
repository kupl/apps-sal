class Solution:

    def minKBitFlips(self, A: List[int], K: int) -> int:
        counter = 0
        q = []
        qL = 0
        for i in range(len(A) - K + 1):
            if A[i] == (len(q) - qL) % 2:
                counter += 1
                q.append(i + K - 1)
            if qL < len(q) and q[qL] == i:
                qL += 1
        for i in range(len(A) - K + 1, len(A)):
            if A[i] == (len(q) - qL) % 2:
                return -1
            if qL < len(q) and q[qL] == i:
                qL += 1
        return counter
