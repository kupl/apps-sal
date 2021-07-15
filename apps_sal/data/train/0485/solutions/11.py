class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        ans = 0
        flips = 0
        addon = 6
        m = False
        for i in range(n):
            if A[i] > 5:
                m = True
                A[i] -= addon
            if (flips % 2 == 0 and A[i] == 0) or (flips % 2 != 0 and A[i] == 1):
                ans += 1
                if i + K > n: return -1
                A[i+K-1] += addon
                flips += 1
            if m or A[i] > 5:
                flips -= 1
                A[i] -= addon
                m = False
        return ans
