class Solution:

    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        if len(A) <= 1:
            return len(A)
        (N, MOD) = (len(A), 10 ** 9 + 7)
        trees = {}
        ans = 0
        A.sort()
        for i in range(N):
            trees[A[i]] = 1
            for j in range(i):
                factor = A[i] / A[j]
                if not factor.is_integer():
                    continue
                factor = int(factor)
                if factor in trees:
                    trees[A[i]] += trees[A[j]] * trees[factor]
            ans += trees[A[i]]
        return ans % MOD
