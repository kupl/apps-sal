class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        k = K
        j = ans = 0
        for i in range(len(A)):
            if not A[i]:
                k -= 1
            while k < 0:
                if not A[j]:
                    k += 1
                j += 1
            ans = max(ans, i - j + 1)
        return ans
