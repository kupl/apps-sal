class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i, j = 0, 0
        count = 0
        out = 0
        for i in range(len(A)):
            if A[i] == 0:
                count += 1
            while count > K and j < len(A):
                if A[j] == 0:
                    count -= 1
                j += 1
            out = max(out, i - j + 1)
        return out
            

