class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l,r = 0, -1
        optim = 0
        while r < len(A):
            while r < len(A):
                r += 1
                if r == len(A):
                    break
                if A[r] == 0:
                    K -= 1
                if K < 0:
                    break
                else:
                    optim = max(optim, r-l+1)
            if r == len(A):
                break
            while l < r:
                if A[l] == 0:
                    K += 1
                l += 1
                if K >= 0:
                    break
        return optim
