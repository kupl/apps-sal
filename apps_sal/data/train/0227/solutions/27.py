class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        right = 0
        for i in range(len(A)):
            if A[i] == 0:
                A[i] = 1
            else:
                A[i] = 0
        tot = A[0]
        res = 0
        for left in range(len(A)):
            while tot <= K:
                right = right + 1
                if right >= len(A):
                    break
                tot = tot + A[right]
            res = max(res, right - left)
            if right >= len(A) - 1:
                break
            if A[left] == 1:
                tot = tot - 1
        return res
