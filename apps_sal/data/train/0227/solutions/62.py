class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:

        windowstart, curr0, res = 0, 0, 0
        currwindow = {1: 0, 0: 0}

        for windowend in range(len(A)):

            currwindow[A[windowend]] += 1
            curr0 = currwindow[0]

            if curr0 > K:
                currwindow[A[windowstart]] -= 1
                windowstart += 1

            res = max(res, windowend - windowstart + 1)

        return res
