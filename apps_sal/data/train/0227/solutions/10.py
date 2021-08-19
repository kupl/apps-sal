class Solution:

    def longestOnes(self, A: List[int], k: int) -> int:
        leftPtr = 0
        rightPtr = 0
        windowSize = []
        while rightPtr <= len(A) - 1:
            if A[rightPtr] == 0:
                k -= 1
            if k < 0:
                if A[leftPtr] == 0:
                    k += 1
                leftPtr += 1
            rightPtr += 1
        return rightPtr - leftPtr
