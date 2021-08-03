class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l = 0
        res = 0
        for h in range(len(A)):
            K -= 1 - A[h]
            if K < 0:
                K += 1 - A[l]
                l += 1
        return h - l + 1
