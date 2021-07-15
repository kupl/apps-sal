class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        d = {}
        Aset = set(A)
        A.sort()
        ans = 0
        for i in range(len(A)):
            d[A[i]] = 1
            for j in range(i):
                if A[i]%A[j] == 0:
                    k = A[i]//A[j]
                    if k in set(A):
                        d[A[i]] += d[A[j]]*d[k]
                        d[A[i]] %= 10**9+7
            ans += d[A[i]]
            ans %= 10**9+7
        return ans

