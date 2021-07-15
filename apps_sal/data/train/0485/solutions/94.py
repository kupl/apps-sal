class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        cur, res, n = 0, 0, len(A)
        for i in range(len(A)):
            if A[i] == (cur % 2):
                if (i + K  > n): return -1 
                res += 1
                cur += 1
                A[i] -= 2
            if (i - K + 1 >= 0) and (A[i-K + 1] < 0):
                cur -= 1
        return res
