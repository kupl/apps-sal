class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        onecount = 0
        start = 0
        ans = 0
        for end in range(len(A)):
            if A[end] == 1:
                onecount += 1
            if end - start + 1 - onecount > K:
                if A[start] == 1:
                    onecount -= 1
                start += 1
            ans = max(ans, end - start + 1)
        return ans
