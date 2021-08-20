class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        a = set(A)
        cache = {}
        ans = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                ans = max(ans, self.helper(a, A[i], A[j], cache))
        return ans if ans > 2 else 0

    def helper(self, a, n1, n2, cache):
        if (n1, n2) not in cache:
            if n1 + n2 not in a:
                cache[n1, n2] = 2
            else:
                cache[n1, n2] = self.helper(a, n2, n1 + n2, cache) + 1
        return cache[n1, n2]
