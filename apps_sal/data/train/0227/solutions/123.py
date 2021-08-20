class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        maxOnes = 0
        start = 0
        maxZeroes = 0
        for i in range(len(A)):
            if A[i] == 0:
                maxZeroes += 1
            while maxZeroes > K:
                if A[start] == 0:
                    maxZeroes -= 1
                start += 1
            maxOnes = max(maxOnes, i - start + 1)
        return maxOnes
