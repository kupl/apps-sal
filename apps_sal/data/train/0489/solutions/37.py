class Solution:

    def maxWidthRamp(self, A: List[int]) -> int:
        n = len(A)
        l = []
        res = 0
        for j in range(n):
            if not l or A[l[-1]] > A[j]:
                l.append(j)
            else:
                (left, right) = (0, len(l) - 1)
                while left < right:
                    mid = (left + right) // 2
                    if A[l[mid]] <= A[j]:
                        right = mid
                    else:
                        left = mid + 1
                res = max(res, j - l[left])
        return res
