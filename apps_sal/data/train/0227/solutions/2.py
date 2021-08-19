"""
[1,1,1,0,0,0,1,1,1,1,0]
           i
                     j
"""


class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        (left, right) = (0, 0)
        alen = len(A)
        while right < alen:
            if A[right] == 0:
                K -= 1
            if K < 0:
                if A[left] == 0:
                    K += 1
                left += 1
            right += 1
        return right - left
