class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        windowstart, most_common, res = 0, 0, 0
        currentwindow = {1: 0, 0: 0}

        for windowend in range(len(A)):

            currentwindow[A[windowend]] += 1

            most_common = currentwindow[1]

            # having this means we have to reduce the length of the window
            if (windowend - windowstart + 1 - most_common > K):

                currentwindow[A[windowstart]] -= 1
                windowstart += 1

            res = max(res, windowend - windowstart + 1)

        return res
