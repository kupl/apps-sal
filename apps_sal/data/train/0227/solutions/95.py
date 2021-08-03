class Solution:
    def longestOnes(self, A, K: int) -> int:
        ans = count = 0
        j = 0  # valid range is [i:j]
        for i in range(len(A)):
            if i > 0 and A[i - 1] == 0:
                count -= 1

            while j < len(A) and (A[j] or count < K):
                if A[j] == 1:
                    j += 1
                elif count < K:
                    count += 1
                    j += 1

            ans = max(ans, j - i)

        return ans
