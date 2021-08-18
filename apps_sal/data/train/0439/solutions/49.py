class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        if n == 0:
            return 0
        if n == 1:
            return 1
        i = 0
        j = 0
        res = 1
        while i < n - 1:

            if (i % 2 == 0 and A[i] < A[i + 1]) or (i % 2 == 1 and A[i] > A[i + 1]) or (i % 2 == 0 and A[i] > A[i + 1]) or (i % 2 == 1 and A[i] < A[i + 1]):
                j = i + 1
                pre_direction = -2
                while j < n:

                    if A[j] > A[j - 1]:
                        direction = 1
                    elif A[j] < A[j - 1]:
                        direction = -1
                    if A[j] == A[j - 1]:
                        i = j
                        break

                    if direction == pre_direction:
                        i = j - 1
                        break
                    pre_direction = direction
                    if j == n - 1:
                        return max(res, j - i + 1)
                    res = max(res, j - i + 1)
                    j += 1
            else:
                i += 1

        return res
