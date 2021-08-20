class Solution:

    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        SA = set(A)
        A = sorted(SA)
        C = {}
        for x in A:
            C[x] = 1
        for (i, x) in enumerate(A):
            for j in range(i):
                if A[j] * A[j] > A[i]:
                    break
                elif A[j] * A[j] == A[i]:
                    C[A[i]] += C[A[j]] * C[A[j]]
                elif A[i] % A[j] == 0 and A[i] // A[j] in SA:
                    C[A[i]] += 2 * C[A[j]] * C[A[i] // A[j]]
        res = sum(C.values())
        return res % (10 ** 9 + 7)
