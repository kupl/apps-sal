class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        """
        for size in range(len(A)-1, -1, -1): 
            i = 0
            j = i+size
            count = 0
            for ind in range(i, j+1):
                if A[ind] == 0: 
                    count += 1

            while j < len(A): 
                if count <= K: 
                    return size+1
                else:
                    if A[i] == 0: count -= 1
                    if j < len(A)-1 and A[j+1] == 0: count += 1
                    j += 1
                    i += 1

        return 0
        """
        maxConsecutiveOnes = 0
        windowStart = 0
        currZeroes = 0
        for windowEnd in range(len(A)):
            if A[windowEnd] == 0:
                currZeroes += 1
            while currZeroes > K:
                if A[windowStart] == 0:
                    currZeroes -= 1
                windowStart += 1
            maxConsecutiveOnes = max(maxConsecutiveOnes, windowEnd - windowStart + 1)
        return maxConsecutiveOnes
