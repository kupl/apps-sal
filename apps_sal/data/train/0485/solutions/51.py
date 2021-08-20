class Solution:

    def minKBitFlips(self, A: List[int], K: int) -> int:
        flip_time = 0
        n = len(A)
        close = [False for i in range(n)]
        res = 0
        for i in range(n):
            if close[i]:
                flip_time -= 1
            if A[i] == 0 and flip_time % 2 == 0 or (A[i] == 1 and flip_time % 2 == 1):
                flip_time += 1
                res += 1
                if i + K > n:
                    return -1
                if i + K < n:
                    close[i + K] = True
        return res
