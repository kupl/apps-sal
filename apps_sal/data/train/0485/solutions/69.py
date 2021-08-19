class Solution:

    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        D = [0] * n
        D[0] = A[0]
        for i in range(n - 1):
            D[i + 1] = A[i + 1] ^ A[i]
        D.append(0)
        cnt = 0
        if D[0] == 0:
            cnt += 1
            D[0] ^= 1
            D[K] ^= 1
        for i in range(1, n - K + 1):
            if D[i] == 1:
                cnt += 1
                D[i] ^= 1
                D[i + K] ^= 1
        D.pop()
        if D == [1] + [0] * (n - 1):
            return cnt
        else:
            return -1
