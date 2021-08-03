class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        res = 0
        start, end = 0, 0
        cnt = 0
        while end < len(A) and start < len(A):
            if A[end] == 1:
                res = max(res, end - start + 1)
                end += 1
            elif A[end] == 0 and cnt < K:
                res = max(res, end - start + 1)
                cnt += 1
                end += 1
            else:
                if A[start] == 0 and K > 0:
                    cnt -= 1
                start += 1
                if start > end:
                    end = start
        return res
