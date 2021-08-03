class Solution:
    def longestOnes(self, A: List[int], k: int) -> int:
        res = 0
        i = j = 0

        move = 1
        while i < len(A) and j < len(A):
            if move == 1:
                if A[j] == 0:
                    if k == 0:
                        move = 0
                        print(i, j)
                        res = max(res, j - i)
                    k -= 1
                j += 1
            if move == 0:
                if A[i] == 0:
                    k += 1
                    move = 1
                i += 1

        return max(res, j - i)
