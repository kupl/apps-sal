class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        (st, ed) = (0, 0)
        ans = 0
        longest = 0
        k = 0
        while ed < len(A):
            while ed < len(A):
                if A[ed] == 1:
                    longest += 1
                elif k < K:
                    k += 1
                    longest += 1
                else:
                    break
                ed += 1
            ans = max(longest, ans)
            while st <= ed and st < len(A):
                longest -= 1
                if A[st] == 0:
                    k -= 1
                    st += 1
                    break
                st += 1
        return ans
