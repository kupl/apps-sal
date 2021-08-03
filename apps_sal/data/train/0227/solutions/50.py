class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        startWindow = 0
        maxLength = 0
        nZerosInsideWindow = 0

        for endWindow, el in enumerate(A):
            nZerosInsideWindow += (el == 0)

            while nZerosInsideWindow > K:
                firstElement = A[startWindow]
                nZerosInsideWindow -= (firstElement == 0)
                startWindow += 1

            maxLength = max(maxLength, endWindow - startWindow + 1)

        return maxLength
