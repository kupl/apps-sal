class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:

        l = 0
        r = 0
        val = 0
        if A[0] == 0:
            val = 1
        maxlength = 0

        while r < len(A) - 1:
            while val <= K and r < len(A) - 1:
                if A[r + 1] == 0:
                    val += 1
                r += 1
            if r == len(A) - 1 and val <= K:
                maxlength = max(maxlength, r - l + 1)
            elif val > K:
                maxlength = max(maxlength, r - l)
                while val > K:
                    if A[l] == 0:
                        val -= 1
                    l += 1

        return maxlength
