class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        result = 0
        zero_allowed = K
        left = 0

        for right, x in enumerate(A):
            if x == 0:
                zero_allowed -= 1
            if zero_allowed >= 0 and (right - left + 1) > result:
                result = right - left + 1

            while zero_allowed < 0 and (right - left + 1) > result:
                if A[left] == 0:
                    zero_allowed += 1
                left += 1

        return result
