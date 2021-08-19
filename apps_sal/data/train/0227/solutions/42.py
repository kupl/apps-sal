class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        l = len(A)
        end = 0
        start = 0
        ans = 0
        count = 0
        for i in range(l):
            if A[i] == 1:
                count += 1
            if end - start + 1 - count <= K:
                ans = max(ans, end - start + 1)
            else:
                if A[start] == 1:
                    count -= 1
                start += 1
            end += 1
        return ans
