class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        ans = 0
        l = 0
        for r in range(len(A)):
            if A[r] == 0:
                K -= 1
            while K < 0:
                if A[l] == 0:
                    K += 1
                l += 1
            ans = max(ans, r + 1 - l)

        return ans
