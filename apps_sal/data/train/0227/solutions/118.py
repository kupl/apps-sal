class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        res = 0
        (j, count0) = (0, 0)
        for i in range(n):
            if not A[i]:
                count0 += 1
                if count0 > K:
                    res = max(res, i - j)
                    while A[j]:
                        j += 1
                    j += 1
                    count0 -= 1
        res = max(res, i - j + 1)
        return res
