class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:

        counter = 0
        i = 0
        j = 0
        res = 0

        for i in range(0, len(A)):

            if A[i] == 0:
                counter += 1

            while counter > K and j < len(A):
                if A[j] == 0:
                    counter -= 1
                j += 1
            res = max(res, i - j + 1)
            print(res)

        return res
