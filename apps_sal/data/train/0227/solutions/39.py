class Solution:

    def longestOnes(self, A: List[int], k: int) -> int:
        ans = 0
        i = 0
        for (j, c) in enumerate(A):
            k -= 1 - c
            if k < 0:
                k += 1 - A[i]
                i += 1
                ans = max(ans, j - i + 1)
        return max(ans, j - i + 1)
