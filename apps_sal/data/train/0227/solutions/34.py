class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        res = 0
        i, j, N = 0, 0, len(A)
        remaining = K if A[i] == 1 else K - 1
        while i < N:
            # resetting
            if i > j:
                j = i
                remaining = K if A[i] == 1 else K - 1

            # stretch
            while j + 1 < N and remaining >= 0:
                if A[j + 1] == 0:
                    if remaining > 0:
                        remaining -= 1
                    else:
                        break
                j += 1
                res = max(res, j - i + 1)

            # pay debt
            if A[i] == 0:
                remaining += 1
            i += 1
        return res
