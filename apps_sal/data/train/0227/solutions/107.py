class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        zeros = 0
        res = 0

        for right in range(len(A)):

            if A[right] == 0:
                zeros += 1

            while zeros > K:
                left += 1
                if A[left - 1] == 0:
                    zeros -= 1

            res = max(res, right - left + 1)

        return res
