class Solution:

    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        memo = {}
        ans = 0
        A.sort()
        for i in range(len(A)):
            localAns = 1
            for j in range(i, -1, -1):
                if A[i] / A[j] in memo:
                    localAns += memo[A[i] / A[j]] * memo[A[j]]
            ans += localAns
            memo[A[i]] = localAns
        return ans % (10 ** 9 + 7)
