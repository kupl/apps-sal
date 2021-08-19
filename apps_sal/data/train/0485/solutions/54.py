class Solution:

    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        cur = 0
        res = 0
        for i in range(n):
            if i >= K and A[i - K] > 1:
                cur -= 1
                A[i - K] -= 2
            if cur % 2 == A[i]:
                if i + K > n:
                    return -1
                cur += 1
                res += 1
                A[i] += 2
        return res
