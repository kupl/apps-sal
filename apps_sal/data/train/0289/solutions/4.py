class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        S = [A[0]]
        for i in range(1, len(A)):
            S.append(S[-1] + A[i])

        def getSum(a, b):
            sm = 0
            for i in range(len(A) - a + 1):
                s = S[i + a - 1] - (S[i - 1] if i > 0 else 0)
                for j in range(i + a, len(A) - b + 1):
                    sm = max(sm, s + S[j + b - 1] - S[j - 1])
            return sm
        return max(getSum(L, M), getSum(M, L))
