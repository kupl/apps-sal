class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        cache = dict()
        iSet = set(A)

        def helper(i):
            if i not in cache:
                count = 1
                for j in range(len(A)):
                    if i != A[j] and i % A[j] == 0:
                        if i // A[j] in iSet:
                            count += helper(A[j]) * helper(i // A[j])
                cache[i] = count
            return cache[i]
        ans = 0
        for i in range(len(A)):
            ans += helper(A[i])
        return ans % 1000000007
