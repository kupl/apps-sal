class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) < 2:
            return len(A)
        if len(A) == 2:
            return 2 if A[0] != A[1] else 1
        DP = [0 for _ in A]
        for i in range(1, len(A)):
            if DP[i - 1] > 1:
                if A[i] > A[i - 1]:
                    DP[i] = -DP[i - 1] - 1
                elif A[i] < A[i - 1]:
                    DP[i] = 2
                else:
                    DP[i] = 1
            elif DP[i - 1] < -1:
                if A[i] < A[i - 1]:
                    DP[i] = -DP[i - 1] + 1
                elif A[i] > A[i - 1]:
                    DP[i] = -2
                else:
                    DP[i] = -1
            elif A[i] == A[i - 1]:
                DP[i] = 1
            else:
                DP[i] = 2 * (-1 if A[i] > A[i - 1] else 1)
        return abs(max(DP, key=abs))
