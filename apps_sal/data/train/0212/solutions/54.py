class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        n = len(A)
        nums = set(A)
        A = sorted(A)
        counts = collections.defaultdict(int)
        mod = 10**9 + 7
        res = 0
        for i, num in enumerate(A):
            for j in range(i):
                b, c = A[j], num / A[j]
                if c in nums:
                    counts[num] += (counts[b] * counts[c]) % mod
            counts[num] += 1
            res = (res + counts[num]) % mod
        return res
