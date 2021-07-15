class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        mapping = {x: i for i, x in enumerate(A)}
        maximal = A[-1]
        N = len(A)
        ans, MOD = [1] * N, 10 ** 9 + 7
        for i in range(N):
            for j in range(i + 1):
                if A[i] * A[j] in mapping and A[i] * A[j] <= maximal:
                    if A[i] != A[j]:
                        ans[mapping[A[i] * A[j]]] += 2 * ans[i] * ans[j]
                    else:
                        ans[mapping[A[i] * A[j]]] += ans[i] * ans[j]
                    ans[mapping[A[i] * A[j]]] %= MOD
        return sum(ans) % MOD
